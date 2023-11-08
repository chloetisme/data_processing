# working with scipy.stats and doing t-tests on microfluidic chips
"""
Created on Tue Nov  7 17:39:04 2023

@author: chloe
"""

import csv
import numpy as np
import scipy.stats as stats
# import matplotlib.pyplot as plt
# import math


#bring in data entire data set as dataframe (df)

results = []

#open csv and store data into arrays from above
with open('Cleaned_Experimental_setup_and_results_results.csv') as File:  
    plots = csv.reader(File) 
    
    for row in plots: 
        results.append(row)
    
###seperate results into each group

# N_DI = results[1] #gets all values in 2nd row (indexing starts at 0)
# N_DI = N_DI[1:21] #gets values from 2 to 22 within the row created
# N_DI =np.array(N_DI, dtype=float) #make the values float

N_DI = np.array(((results[1])[1:13]), dtype=float) #combining steps above 
N_PL = np.array(((results[2])[1:17]), dtype=float)
N_PH = np.array(((results[3])[1:17]), dtype=float)
BL_DI = np.array(((results[4])[1:17]), dtype=float)
BL_PL = np.array(((results[5])[1:13]), dtype=float)
BL_PH = np.array(((results[6])[1:21]), dtype=float)

#let's get to t-testing https://www.youtube.com/watch?v=CIbJSX-biu0
#two sample T-test

stats.ttest_ind(a=BL_DI, b=BL_PL, equal_var=False)


#not getting a result, could be that I don't have commas between my values?