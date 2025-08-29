# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 13:04:52 2025

@author: peake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_path = "" # insert the path to the folder here
lines_file = pd.read_csv(folder_path+"lines.csv")
pos_file = pd.read_csv(folder_path+"position.csv")
lum_ratios = np.load(folder_path+"luminosity_ratios.npy") # array of line ratios at each position 

def line_finder(element,state,lines): # finds lines of a given element & ionization state
    lines_found_index = []
    for i,line in enumerate(lines):
        if line.split()[0] == element and line.split()[1] == state:
            lines_found_index.append(i)
    lines_found = lines.iloc[lines_found_index]
    return lines_found

lines = lines_file['Lines'] # series of all the lines
pos = pos_file['Distance [pc]'] # array of positions from the OB star 
FUV = pos_file['FUV [G0]'] # array of the FUV field in G0 at each position

element = 'N' # choose element
state = '2' # choose ionization state as a number e.g. 2=II in this case
lines_NII = line_finder(element,state,lines) # returns a series of lines found 

element = 'S' # choose element
state = '2' # choose ionization state as a number e.g. 2=II in this case
lines_SII = line_finder(element,state,lines) # returns a series of lines found 

# choose the indices from lines found using the line finder function
index1 = 5401 # top of ratio
index2 = 1143 # bottom of ratio
plt.plot(pos,lum_ratios[:,index1,index2]) # could choose to plot against FUV instead
plt.yscale('log'); plt.ylabel('Line Ratio'); plt.xlabel('Distance [pc]'); plt.title(f'{lines[index1]}  /  {lines[index2]}')














