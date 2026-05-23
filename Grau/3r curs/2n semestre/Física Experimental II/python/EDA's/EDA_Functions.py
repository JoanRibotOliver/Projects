from sys import exit

import numpy as np
import matplotlib.pyplot as plt
from EDA_Number_Rounder import EDA_NR

# EDAs is an EDA object or a list of them, data in {'xy', 'experimental', 'both'}. 
# data = 'experimental' works only with 2 variables
def EDA_Tablemaker(EDAs, data = 'xy', singlecol = False):
    W = 60   # Width of console 
    def title(string): print(); print("-"*W); print(" "*round((W - len(string))/2) + string); print()
    def print_table(table):
        # Get index of columns with shared uncertainty
        indexes = []
        for j in range(len(table.T)):
            errors = [value.split(' ± ')[1] for value in table.T[j]]
            if all(error == errors[0] for error in errors): indexes.append(j)

        # Save shared uncertainties
        uncertainties = [table.T[j][0].split(' ± ')[1] for j in indexes]
        
        # Remove uncertainty of those columns
        for j in indexes:
            for i, value in np.ndenumerate(table.T[j]): table[i,j] = value.split(' ± ')[0]
        
        # singlecol functionality for single EDA
        if singleEDA and singlecol: 
            for i in (table.T[0] if singlecol == 'x' else table.T[1]): print(i)
            for j, error in zip(indexes, uncertainties):
                if j == {'x': 0, 'y': 1}[singlecol]: print(f"\nUncertainty is: {error}")
        else:
            for row in table: print("	".join(row))
            print()
            for i in [f"Uncertainty of column {j+1}: {error}" for j, error in zip(indexes, uncertainties)]: print(i)
    
    ## Compatibility with a single EDA
    if type(EDAs) is not list: singleEDA = True; EDAs = [EDAs]
    elif len(EDAs) == 1: singleEDA = True
    else: singleEDA = False 
    
    ## Actuall data printing
    if data == 'xy':
        # Get columns
        xcols = np.array([EDA.x_rounded for EDA in EDAs], dtype = object)
        ycols = np.array([EDA.y_rounded for EDA in EDAs], dtype = object)
    
        # Verify that all x columns are shared
        if not np.all(xcols == xcols[0]): print("x columns not matching"); exit()
        
        # Create table and process shared uncertainties
        table = np.insert(ycols.T, 0, xcols[0], axis = 1)

        # Print
        if singleEDA and singlecol: title(f"Word Table of {singlecol}")
        else: title("Word Table of x and " + ("multiple " if not singleEDA else "") + "y")
        print_table(table)
        
    elif data == 'experimental':
        # Check if all EDAs have same keys
        keys_list = [sorted(list(EDA.MEASURES_rounded.keys())) for EDA in EDAs]
        if not all(keys_list[0] == keys for keys in keys_list): print("Not same measures"); exit()
        if not all(len(keys) == 2 for keys in keys_list): print("More than two keys"); exit()
        keys = list(EDAs[0].MEASURES_rounded.keys())
        
        # Get shared (x) and variable (y) keys
        for key in keys:
            if all(EDA.MEASURES_rounded[key] == EDAs[0].MEASURES_rounded[key] for EDA in EDAs): xkey = key; break
        keys.remove(xkey); ykey = keys[0]
        
        # Create table
        ycols = np.array([EDA.MEASURES_rounded[ykey] for EDA in EDAs], dtype = object)
        table = np.insert(ycols.T, 0, EDAs[0].MEASURES_rounded[xkey], axis = 1)

        # Print
        if singleEDA and singlecol: title("Word Table of " + (f"{xkey}" if singlecol == 'x' else f'{ykey}'))
        else: title(f"Word Table of {xkey} and " + ("multiple " if not singleEDA else "") + f"{ykey}")
        print_table(table)        
        
    elif data == 'both':
        EDA_Tablemaker(EDAs, 'xy', singlecol = singlecol)
        EDA_Tablemaker(EDAs, 'experimental', singlecol = singlecol)

# EDAs is a list of EDA objects; plotargs is a list containing the keyargs for each plot in a dictionary.
def EDA_multiplotter(EDAs, plotargs):
    fig, ax = plt.subplots()
    for i, EDA in enumerate(EDAs): EDA.plot(given_fig = fig, given_ax = ax, **plotargs[i])
    plt.show()