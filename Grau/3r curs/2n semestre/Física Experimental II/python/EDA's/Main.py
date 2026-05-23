import numpy as np
#import sys; sys.path.append('D:/FonerBalear (Usuari)/Google Drive/Programming/1 - Physics/1 - EDA')
from Experimental_Data_Analysis import EDA
# from EDA_Functions import EDA_Tablemaker
# from EDA_NR import ufloat_rounder, uarray_average

from Multiplotter import Multiplotter
from Tablemaker import TablemakerLatex

Experiment = EDA(XY_Equations = {'x': '1/λ**2', 'y': 'sy.sin((θ+α)/2)/sy.sin(α/2)'}, parameter_eq = "TEST = A/B",
                 δy_quadratic = True, δx_quadratic = True, lr = True, printing = True, δchoice = "Ask", exclude = None,
                 CONSTANTS = {'α': np.radians(60), 'δα': np.radians(1/60), 'δλ': (10**(-3))*0.1, 'δθ': np.radians(1/60)},
                 MEASURES = {'θ': np.radians(np.array([23+10/60, 23+15/60, 23+23/60, 23.5+20/60, 23.5+29/60, 23+17/60, 23.5+1/60, 23.5+6/60, 23.5+9/60])),
                             'λ': (10**(-3))*np.array([690.7, 614.5, 546.1, 435.8, 404.7, 643.8, 508.6, 467.8, 441.6])})

#TablemakerLatex(Experiment)

#Multiplotter(Experiment)

Experiment.latex_equations()

Experiment.plot(given_fig = None, given_ax = None, unit_scale = (1, 1), x_lim = 'auto', y_lim = 'auto', point_color = 'dodgerblue', error_color = 'black', regression_color = 'black',
                title = "", x_label = "NO SURT LA REGRESSIÓ... ERROR AX.AXLINE?", y_label = "MODIFICAR PARÀMETRES SEGONS CONVENGUI", point_label = "GIVE ME SOMETHING", lr_label = "GIVE ME SOMETHING", y_offset = 0,
                grid = True, grid_minor = False, legend_loc = 'best', lines = False, lr_B_errorbars = False, margins_from = 'errors', margin_percentage = 15,
                x_ticks = 'Auto', y_ticks = 'Auto', xy_ticks_decimals = 'Auto', min_max_major_ticks = [6, 'Auto'], minor_ticks = True, n_minor_ticks = 'Auto',
                filename = "graph", dpi = 600, save = False, open_it = False)



# Provar programa a l'spider...
