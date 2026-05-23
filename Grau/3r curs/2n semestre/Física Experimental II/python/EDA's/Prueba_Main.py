import numpy as np
import sys; sys.path.append('D:/FonerBalear (Usuari)/Google Drive/Programming/1 - Physics/1 - EDA')
from Experimental_Data_Analysis import EDA
# from EDA_Functions import EDA_Tablemaker
# from EDA_NR import ufloat_rounder, uarray_average

Experiment = EDA(XY_Equations = {'x': 'Δ', 'y': 'm*g'}, parameter_eq = "TEST = A/B",
                 δy_quadratic = True, δx_quadratic = True, lr = True, printing = True, δchoice = "Ask", exclude = None,
                 CONSTANTS = {'g': 9.81, 'δg': 0.01,'δΔ': 0.001},
                 MEASURES = {'m': np.array([0.05069, 0.10118, 0.15497, 0.20618, 0.2566,	0.3072, 0.359, 0.40963, 0.45997, 0.51042, 0.56105, 0.61165, 0.66219]),
                             'δm': 0.00086*np.array([0.05069, 0.10118, 0.15497, 0.20618, 0.2566,	0.3072, 0.359, 0.40963, 0.45997, 0.51042, 0.56105, 0.61165, 0.66219]),
                             'Δ': np.array([0.005, 0.01, 0.015, 0.02, 0.028, 0.034, 0.038, 0.045, 0.05, 0.059, 0.060, 0.06700, 0.06800])})

Experiment.plot(given_fig = None, given_ax = None, unit_scale = (1, 1), x_lim = 'auto', y_lim = 'auto', point_color = 'dodgerblue', error_color = 'black', regression_color = 'black',
                title = "F vs Δx", x_label = "Δx", y_label = "Fg", y_offset = 0,
                grid = True, grid_minor = False, legend_loc = 'best', lines = False, lr_B_errorbars = False, margins_from = 'errors', margin_percentage = 15,
                x_ticks = 'Auto', y_ticks = 'Auto', xy_ticks_decimals = 'Auto', min_max_major_ticks = [6, 'Auto'], minor_ticks = True, n_minor_ticks = 'Auto',
                filename = "graph", dpi = 600, save = False, open_it = False)

Experiment.latex_equations()