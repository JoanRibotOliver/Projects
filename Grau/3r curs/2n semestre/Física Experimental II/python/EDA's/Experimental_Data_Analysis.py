# By Felip Antoni Ramis Vidal
# Version 5.0

'''
##  Usage comments  ##
· Can give None to parameter_eq.
· Give all units in S.I and then change unit_scale in plot.
· margins_percentage is percentage of figure length to be occupied by margins in both x and y directions.

##  Input Examples  ##
· XY_Equations = {'y':'sy.sin((θ+α)/2)/sy.sin(α/2)', 'x':'1/λ**2'}
· parameter_eq = "TEST = A/B"
· CONSTANTS = {'α': np.radians(60), 'δα': np.radians(1/60), 'δλ': (10**(-3))*0.1, 'δθ': np.radians(1/60)}
· MEASURES = {'θ': np.radians(np.array([23+10/60, 23+15/60, 23+23/60, 23.5+20/60, 23.5+29/60, 23+17/60, 23.5+1/60, 23.5+6/60, 23.5+9/60])),
              'λ': (10**(-3))*np.array([690.7, 614.5, 546.1, 435.8, 404.7, 643.8, 508.6, 467.8, 441.6])}
'''

from ftplib import MAXLINE
from sys import exit
import numpy as np; import sympy as sy
from EDA_Number_Rounder import EDA_NR
# from shutil import get_terminal_size

# import matplotlib
import matplotlib.pyplot as plt
from IPython.display import display
from matplotlib.ticker import (FormatStrFormatter, AutoMinorLocator, MaxNLocator)  # MultipleLocator, AutoMinorLocator
# from IPython import get_ipython; get_ipython().run_line_magic('matplotlib', 'inline')  #'qt5 (or qt4)' for interactive, 'inline' for inline

plt.rcParams.update({"font.family": "Times New Roman", "mathtext.fontset": "cm"})
plt.rcParams.update({"lines.linewidth": 0.8, "lines.markersize": 0.8})
plt.rcParams['figure.dpi'] = 120; plt.rcParams['axes.formatter.useoffset'] = False

## Global variables for memory
Last_Figure = None; EDA_Points = []

## Class Definition
class EDA():
    def __init__(self, *, XY_Equations, parameter_eq = None, CONSTANTS, MEASURES, exclude = None, lr = True,
                 δy_quadratic = True, δx_quadratic = True, δparameter_quadratic = True, δchoice = "Ask", printing = True):

        ## Initial checks
        lenghts = [len(MEASURES[key]) for key in MEASURES]
        if not np.array(lenghts).all(): print("Given empty data arrays"); exit()
        
        if (np.array(lenghts) == np.array(lenghts)[0]).all(): self.N = lenghts[0]
        else: print("Lenghts of MEASURES arrays do not match"); exit()
                
        if np.array([isinstance(cnt, (list, tuple, np.ndarray)) for cnt in CONSTANTS.values()]).any(): print("Arrays go in 'MEASURES'"); exit()
        if type(exclude) == int: exclude = [exclude]
        exclude_bool = False if exclude is None else True
        
        # Change str equation into a list with [0] = parameter name and [1] = parameter equation
        if isinstance(parameter_eq, str): parameter_eq = parameter_eq.replace(" ","").split("=")
        elif parameter_eq is not None: print("ERROR: Invalid parameter_eq"); exit()
        
        # Saving stuff for some defs
        self.MEASURES, self.CONSTANTS = MEASURES, CONSTANTS
        self.MC = MC = {**MEASURES, **CONSTANTS}
        self.lr = lr; self.parameter_eq = parameter_eq
        self.exclude, self.exclude_bool = exclude, exclude_bool
        self.δchoice = δchoice
        
        # Check if A and/or B have been used as variables/constants
        if 'A' in MC or 'B' in MC: print("A or B are reserved for Linear Regression"); exit()
        
        ##  Variables / Uncertanty / Data substitution                                              
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        # Defining variables
        A, B = sy.symbols("A, B", real=True); δA, δB = sy.symbols("δA, δB", real = True, positive = True)
        
        self.variables = [A, B]; self.δvariables = [δA, δB]  # CONSTANTS are also included
        for key in MC:
            if key[0] != 'δ':
                positive = True if (np.array(MC[key]) >= 0).all() else None
                exec("{0} = sy.Symbol('{0}', real = True, positive = {1})".format(key, positive))
                exec("{0} = sy.Symbol('{0}', real = True, positive = True)".format("δ"+key))
                exec("self.variables.append({})".format(key)); exec("self.δvariables.append({})".format("δ"+key))
        
        for key in XY_Equations: exec("self.eq{} = {}".format(key, XY_Equations[key]))
        self.XY = {'x': [self.eqx]*self.N, 'y': [self.eqy]*self.N}
        
        # Propagation of uncertainty
        self.eqδx = self.propagation_of_uncertainty(self.eqx, δx_quadratic)
        self.eqδy = self.propagation_of_uncertainty(self.eqy, δy_quadratic)
        self.δXY = {'x': [self.eqδx]*self.N, 'y': [self.eqδy]*self.N}
        
        # Data substitution
        for key in self.XY: self.XY[key] = self.data_substitution(self.XY[key])
        for key in self.δXY: self.δXY[key] = self.data_substitution(self.δXY[key])
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        
        ##  Rounding Data
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        # Rounding experimental data
        self.MEASURES_rounded = {}
        for key in MEASURES.keys():
            if key[0] != 'δ':
                errors = MEASURES['δ'+key] if 'δ'+key in MEASURES.keys() else len(MEASURES[key])*[CONSTANTS['δ'+key]]
                self.MEASURES_rounded[key] = [EDA_NR(value, error, experimental = True) for value, error in zip(MEASURES[key], errors)]
                
        # Rounding x and y
        self.x_rounded = [EDA_NR(x, δx) for x, δx in zip(self.XY['x'], self.δXY['x'])]
        self.y_rounded = [EDA_NR(y, δy) for y, δy in zip(self.XY['y'], self.δXY['y'])]
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        
        
        ##  Parameter Equations
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        if self.parameter_eq:
            exec("self.peq = {}".format(parameter_eq[1]))
            self.δpeq = self.propagation_of_uncertainty(self.peq, δparameter_quadratic)
        # --------------------------------------------------------------------------------------------------------------------------------------- 
                
        ##  Exclude Functionality
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        if exclude_bool:
            # Save excluded
            self.excludedXY = {'x': np.array([self.XY['x'][i] for i in exclude]), 'y': np.array([self.XY['y'][i] for i in exclude])}
            self.excludedδXY = {'x': np.array([self.δXY['x'][i] for i in exclude]), 'y': np.array([self.δXY['y'][i] for i in exclude])}
            
            # Delete excluded points from self.XY and self.δXY
            self.XY['x'], self.XY['y'] = np.delete(self.XY['x'], exclude), np.delete(self.XY['y'], exclude)
            self.δXY['x'], self.δXY['y'] = np.delete(self.δXY['x'], exclude), np.delete(self.δXY['y'], exclude)
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        
        
        ##  Calling Lineal Regression
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        if lr == True:
            # Check if wlr
            wlr = False
            for key in self.δXY:
                if not (self.δXY[key] == self.δXY[key][0]).all(): wlr = True
            
            # Printings 1 and 2: Start, Equations, Values & Results 1
            if printing: self.printing(1); self.printing(2)
            
            # Actuall calling
            if wlr:
                min_iterations = 100; max_iterations = 1000; threshold = 10**(-10)
                self.linear_regression(self.XY['x'], self.XY['y'], sigma_x = self.δXY['x'].mean(), sigma_y = self.δXY['y'].mean(), for_wlr = True)
                A0, δA0 = self.A, self.δA; B0, δB0 = self.B, self.δB
                for i in range(1, max_iterations + 1):
                    self.wlr(self.XY['x'], self.XY['y'], sigma_x = self.δXY['x'], sigma_y = self.δXY['y'], B0 = B0)
                    if i > min_iterations and (np.abs([self.A - A0, self.B - B0, self.δA - δA0, self.δB - δB0]) <= threshold).all(): break
                    A0, δA0 = self.A, self.δA; B0, δB0 = self.B, self.δB
                if i == max_iterations: print("The iterative proces does not converge"); exit()
            else: self.linear_regression(self.XY['x'], self.XY['y'], sigma_x = self.δXY['x'].mean(), sigma_y = self.δXY['y'].mean())
            
            # Parameter substitution
            if self.parameter_eq:
                self.parameter = self.peq.subs(A, self.A).subs(B, self.B).subs(δA, self.δA).subs(δB, self.δB).evalf()
                self.δparameter = self.δpeq.subs(A, self.A).subs(B, self.B).subs(δA, self.δA).subs(δB, self.δB).evalf()
                for var in list(self.parameter.atoms(sy.Symbol)): self.parameter = self.parameter.subs(var, CONSTANTS[str(var)])
                for var in list(self.δparameter.atoms(sy.Symbol)): self.δparameter = self.δparameter.subs(var, CONSTANTS[str(var)])
                self.parameter, self.δparameter = np.float64(self.parameter), np.float64(self.δparameter)
                
            # Rounding A, B and parameter
            self.A_rounded, self.B_rounded = EDA_NR(self.A, self.δA), EDA_NR(self.B, self.δB)
            if self.parameter_eq: self.parameter_rounded = EDA_NR(self.parameter, self.δparameter)
            
            # Printing 3: Results 2
            if printing: self.printing(3)
            
        elif (lr == False) and (printing == True): self.printing(1)  # Printing 1: Start, Equations & Values
        # --------------------------------------------------------------------------------------------------------------------------------------- 
        
    def lr_print(self): self.printing(3)
    def latex_equations(self): self.printing("LaTeX")
    def printing(self, n):
        W = 70   # Width of console 
        def title(string): print(" "*round((W - len(string))/2) + string)
        def latex(x): return sy.latex(x).replace("δ", "\delta ")
        
        if n == 1:  # Start, Equations & Values
            # Start        
            print("-"*W); title("EXPERIMENTAL DATA ANALYSIS"); print("-"*W)
            print("-"*W); title("EQUATIONS")        
            
            # Equations
            sy.init_printing()
            print("Equations of x and δx")
            display(sy.Symbol(latex(sy.Eq(sy.Symbol('x'), self.eqx)) + ",\quad" + latex(sy.Eq(sy.Symbol('δx'), self.eqδx))))
            
            print("\n"); print("Equations of y and δy")
            display(sy.Symbol(latex(sy.Eq(sy.Symbol('y'), self.eqy)) + ",\quad" + latex(sy.Eq(sy.Symbol('δy'), self.eqδy))))

            if self.parameter_eq:
                print("\n"); print("Equations of {0} and δ{0}".format(self.parameter_eq[0]))
                display(sy.Symbol(latex(sy.Eq(sy.Symbol(self.parameter_eq[0]), self.peq)) + ",\quad" + latex(sy.Eq(sy.Symbol('δ'+self.parameter_eq[0]), self.δpeq))))
            sy.init_printing(pretty_print = False)
            
            # Values
            print(); print("-"*W); title("VALUES OF X & Y")
            l = round((W - 12)/4); print(" "*l + "x ± δx" + " "*(2*l) + "y ± δy")
            for x, y in zip(self.x_rounded, self.y_rounded):
                x_rounded, δx_rounded = x.split(" ± "); y_rounded, δy_rounded = y.split(" ± ")
                l1 = (l+3) - 2 - len(x_rounded); l2 = 2*(l+3) - len(y_rounded) - len(δx_rounded) - 3        # Measurements
                print(" "*l1 + x + " "*l2 + y)
            print()
            
        elif n == 2: print("-"*W); title("LINEAR REGRESSION")
        
        elif n == 3:
            print("R = {:.12f}".format(round(self.R, 12)) + " "*(W-37) + "R² = {:.12f}".format(round(self.R**2, 12))); print()
            print("A = " + self.A_rounded); print("B = " + self.B_rounded)
            def add_parentheses(string): return string if '(' in string else '(' + string + ')'
            print(f"y = {add_parentheses(self.B_rounded)}*x + {add_parentheses(self.A_rounded)}"); print()
            if self.parameter_eq: print("{} = {}".format(self.parameter_eq[0], self.parameter_rounded))
            
        elif n == "LaTeX":
            print(); print("-"*W); title("LaTeX Equations"); print()
            print(latex(sy.Eq(sy.Symbol('δx'), self.eqδx))); print()
            print(latex(sy.Eq(sy.Symbol('δy'), self.eqδy))); print()
            if self.parameter_eq: print(latex(sy.Eq(sy.Symbol('δ{}'.format(self.parameter_eq[0])), self.δpeq)))
        
    def propagation_of_uncertainty(self, eq, quadratic):
        def normal_term(eq, var, δvar): return sy.Abs(sy.diff(eq, var) * δvar)
        def quadratic_term(eq, var, δvar): return (sy.diff(eq, var) * δvar)**2
        term = quadratic_term if quadratic else normal_term
        
        temp = 0
        for var, δvar in zip(self.variables, self.δvariables):
            if str(δvar) in self.CONSTANTS:
                if self.CONSTANTS[str(δvar)] == 0: continue
            temp += term(eq, var, δvar)
        if quadratic: temp = sy.sqrt(temp)
        return temp.simplify()

    def data_substitution(self, onto):  # 'onto' must be an homogeneous list of sympy expressions
        variables = list(onto[0].atoms(sy.Symbol))
        for i in range(self.N):
            for var in variables:
                if str(var) in self.CONSTANTS.keys(): onto[i] = onto[i].subs(var, self.CONSTANTS[str(var)])
                else: onto[i] = onto[i].subs(var, self.MEASURES[str(var)][i])
        return np.float64(onto)
    
    def linear_regression(self, x, y, sigma_x, sigma_y, for_wlr = False):
        # Ajust lineal a una recta y = A + Bx en el cas de incerteses constants
        TEMP = np.size(x)*np.sum(x**2)-(np.sum(x))**2
        A = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/TEMP
        B = (np.size(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/TEMP
        
        error = self.lr_uncertanties(x, y, sigma_x, sigma_y, A, B, for_wlr)
        
        δA = error * np.sqrt(np.sum(x**2)/TEMP)
        δB = error * np.sqrt(np.size(x)/TEMP)
        
        self.A = A; self.B = B; self.δA = δA; self.δB = δB
        self.R = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sqrt(np.sum((x - np.mean(x))**2) * np.sum((y - np.mean(y))**2))

    def lr_uncertanties(self, x, y, sigma_x, sigma_y, A, B, for_wlr):
        sigma_y_est = np.sqrt((1/(np.size(x)-2)) * np.sum((y - B*x - A)**2))
        sigma_y_equiv = np.sqrt(sigma_y**2 + (B*sigma_x)**2)
       
        if for_wlr: return sigma_y_equiv
        
        def ask():
            print(f"\nδy_est = {sigma_y_est}\nδy_exp = {sigma_y}\nδy_eqv = {sigma_y_equiv}")
            choice = str(input("Choose your error for δy: est, exp, eqv: ")); print()
            return choice
         
        choice = ask() if self.δchoice.lower() == 'ask' else self.δchoice
        choice_maker = {'est': sigma_y_est, 'exp': sigma_y, 'eqv': sigma_y_equiv}
        
        if choice in choice_maker.keys(): return choice_maker[choice]
        else: print("ERROR: Invalid Input"); exit()

    def wlr(self, x, y, sigma_x, sigma_y, B0):
        # Ajust lineal a una recta y = A + Bx en el cas de incerteses variables
        wi = 1/(np.square(B0*sigma_x) + np.square(sigma_y))
        wi_xi_yi = np.sum(x * y * wi)
        wi_xi = np.sum(x * wi)
        wi_xi_squared = np.sum(np.square(x) * wi)
        wi_yi = np.sum(y * wi)
        
        Δ = np.sum(wi) * wi_xi_squared - np.square(wi_xi)
        A = (np.sum(wi * x**2)*np.sum(wi * y)-np.sum(wi*x)*np.sum(wi*x*y))/Δ
        B = ((np.sum(wi) * wi_xi_yi) - (wi_xi * wi_yi))/Δ
        δA = np.sqrt(np.sum(wi*x**2)/Δ)
        δB = np.sqrt(np.sum(wi)/Δ)
        
        self.A = A; self.B = B; self.δA = δA; self.δB = δB
        
    def plot(self, given_fig = None, given_ax = None, unit_scale = (1, 1), x_lim = 'auto', y_lim = 'auto', point_color = 'dodgerblue', error_color = 'black', regression_color = 'black',
             title = "", x_label = "Per canviar paràmetres del gràfic line 286", y_label = "GIVE ME SOMETHING", point_label = "", lr_label = "", y_offset = 0,
             grid = True, grid_minor = False, legend_loc = None, lines = False, lr_B_errorbars = False, margins_from = 'errors', margin_percentage = 15,
             x_ticks = 'Auto', y_ticks = 'Auto', xy_ticks_decimals = 'Auto', min_max_major_ticks = [6, 'Auto'], minor_ticks = True, n_minor_ticks = 'Auto',
             filename = "graph", dpi = 600, save = False, open_it = False):
        
        ## Simplify notation
        x, δx = self.XY['x'], self.δXY['x']; y, δy = self.XY['y'], self.δXY['y']
        if self.exclude_bool: ex_x, δex_x = self.excludedXY['x'], self.excludedδXY['x']; ex_y, δex_y = self.excludedXY['y'], self.excludedδXY['y']
        if self.lr: A, B = self.A, self.B; δB = self.δB
        
        ## Scale units functionality
        sx, sy = unit_scale
        if sx != 1:
            x, δx = sx*x, sx*δx
            if self.exclude_bool: ex_x, δex_x = sx*ex_x, sx*δex_x
            if self.lr: B, δB = B/sx, δB/sx
        if sy != 1:
            y, δy = sy*y, sy*δy
            if self.exclude_bool: ex_y, δex_y = sy*ex_y, sy*δex_y
            if self.lr: A, B = sy*A, sy*B
        
        ## Offset Functionality
        if y_offset:
            y = y + y_offset
            if self.exclude_bool: ex_y = ex_y + y_offset
            if self.lr: A = A + y_offset
        
        ## Create axis
        if given_fig and given_ax: fig, ax = given_fig, given_ax
        else: fig, ax = plt.subplots()
        
        ## Plot errorbars
        points, errors, _ = ax.errorbar(x, y, xerr = δx, yerr = δy, marker = 'o', color = point_color, ecolor = error_color, label = point_label, 
                                        capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "--" if lines else "", zorder = 10)
        
        if self.exclude_bool:
            epoints, eerrors, _  = ax.errorbar(ex_x, ex_y, xerr = δex_x, yerr = δex_y, fmt = 'x', color = point_color, ecolor = error_color,
                                               capsize = 2, capthick = 0.4, elinewidth = 0.4, linestyle = "", markersize = 5, zorder = 10)
        
        ## Locate major ticks
        min_major_ticks = min_max_major_ticks[0]
        if min_max_major_ticks[1] in ['Auto', 'auto']: max_major_bins = 'auto'   # Make sure auto is lowercase
        elif isinstance(min_max_major_ticks[1], int): max_major_bins = min_max_major_ticks[1] + 1
        
        try: ax.set_xticks(x_ticks)
        except: ax.xaxis.set_major_locator(MaxNLocator(nbins = max_major_bins, steps = [1, 2, 2.5, 5, 10], min_n_ticks = min_major_ticks))
        try: ax.set_yticks(y_ticks)
        except: ax.yaxis.set_major_locator(MaxNLocator(nbins = max_major_bins, steps = [1, 2, 2.5, 5, 10], min_n_ticks = min_major_ticks))
        # MaxNLocator with the used parameters behaves exactly as AutoLocator() but adding a minimim number of ticks
        
        ## Set limits
        # ----------------------------------------------------------------------------------------------------------
        global Last_Figure, EDA_Points
        if fig != Last_Figure: EDA_Points = []
        EDA_Points.extend([points] if margins_from == 'points' else errors)
        if self.exclude_bool: EDA_Points.extend([epoints] if margins_from == 'points' else eerrors)
        Last_Figure = fig
        
        μ = margin_percentage
        if x_lim in ['Auto', 'auto', None]:
            ax_x = np.hstack([i.get_xdata() for i in EDA_Points])
            xmax, xmin = ax_x.max(), ax_x.min(); Mx = 0.5*μ/(100 - μ)*abs(xmax-xmin); x_lim = (xmin - Mx, xmax + Mx)
        ax.set_xlim(x_lim)
        
        if y_lim in ['Auto', 'auto', None]:
            ax_y = np.hstack([i.get_ydata() for i in EDA_Points])
            ymax, ymin = ax_y.max(), ax_y.min(); My = 0.5*μ/(100 - μ)*abs(ymax-ymin); y_lim = (ymin - My, ymax + My)
        ax.set_ylim(y_lim)
        # ----------------------------------------------------------------------------------------------------------
        
        ## Grid
        if grid: ax.grid(visible = True, linestyle = '--', linewidth = 0.4, alpha = 0.6, zorder = 1)
        if grid_minor: ax.grid(visible = True, which = 'minor', linewidth = 0.2)
        
        ## Locate minor ticks
        if minor_ticks:
            if n_minor_ticks in ['Auto', 'auto']: n_minor_bins = None
            elif isinstance(n_minor_ticks, int): n_minor_bins = n_minor_ticks + 1
            
            ax.yaxis.set_minor_locator(AutoMinorLocator(n_minor_bins))
            ax.xaxis.set_minor_locator(AutoMinorLocator(n_minor_bins))
        
        ## Format ticks
        if isinstance(xy_ticks_decimals, int):
            ax.xaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(xy_ticks_decimals[0])))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(xy_ticks_decimals[1])))
        
        ## Text
        plt.title(title, fontdict = {'fontsize': 12, 'fontweight': 'medium'})
        plt.xlabel(x_label, fontsize = 12); plt.ylabel(y_label, fontsize = 12)
        
        ## Lineal regression
        if self.lr:
            ax.set_xlim(auto = False); ax.set_ylim(auto = False)
            #ax.axline((0, A), slope = B, color = regression_color, label = lr_label)
            
            if lr_B_errorbars:
                ax.plot(x, (B - δB)*x + A, '--', color = "orange", linewidth = 0.5, alpha = 0.8)
                ax.plot(x, (B + δB)*x + A, '--', color = "orange", linewidth = 0.5, alpha = 0.8)
        
        ## Legend
        if point_label or lr_label:
            if grid:
                ax.legend(fancybox = False, shadow = True, edgecolor = 'black', loc = legend_loc)
                ax.get_legend().get_frame().set_linewidth(0.6)
            else: ax.legend(edgecolor = 'white', loc = legend_loc)
        
        ## Save, open, show (if not given axis)
        if not (given_fig or given_ax):
            if save: fig.savefig(filename + ".png", dpi = dpi)
            if open_it: from PIL import Image; Image.open(filename + ".png").show()
            plt.show()

        
if __name__ == "__main__":
    TEST = EDA(XY_Equations = {'y':'sy.sin((θ+α)/2)/sy.sin(α/2)', 'x':'1/λ**2'}, parameter_eq = "Z = A/B",
               CONSTANTS = {'α': np.radians(60), 'δα': np.radians(1/60), 'δλ': (10**(-3))*0.1, 'δθ': np.radians(1/60)},
               MEASURES = {'θ': np.radians(np.array([23+10/60, 23+15/60, 23+23/60, 23.5+20/60, 23.5+29/60, 23+17/60, 23.5+1/60, 23.5+6/60, 23.5+9/60])),
                           'λ': (10**(-3))*np.array([690.7, 614.5, 546.1, 435.8, 404.7, 643.8, 508.6, 467.8, 441.6])})
    TEST.plot()
    TEST.latex_equations()