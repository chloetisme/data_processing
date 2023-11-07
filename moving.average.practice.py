# Working to learn how to use moving average to smooth data
"""
Created on Mon Nov  6 16:23:46 2023

@author: chloe
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

###bring in and plot original data from local .csv

#create a empty arrays for the data to be stored
frame = []
sqrtframe = []
ch1 = []
ch2 = []
ch3 = []
ch4 = []

#open csv and store data into arrays from above
with open('nothing.DI.mp4 - simple import sqrt Cleaned_Th150.csv') as File:  
    plots = csv.reader(File) 
    
    for row in plots: 
        frame.append(float(row[0])) 
        sqrtframe.append(float(row[1])) 
        ch1.append(float(row[2])) 
        ch2.append(float(row[3])) 
        ch3.append(float(row[4])) 
        ch4.append(float(row[5])) 

#plot data on single graph        
plt.plot(sqrtframe, ch1, label= 'Channel 1') 
#plt.plot(sqrtframe, ch2, label= 'Channel 2')
#plt.plot(sqrtframe, ch3, label= 'Channel 3')
#plt.plot(sqrtframe, ch4, label= 'Channel 4')     

#add labels and title to graphs

plt.legend()
plt.xlabel('square root of frame')
plt.ylabel('distance (pixels)')
plt.title('Flow profile of four channel microfluidic chip')
plt.show

#now for the moving average (rolling mean) part

ch1rolling = []
window_size = 100 #how many points are being averaged together
for i in range(len(ch1) - window_size + 1):
    window = ch1[i : i + window_size]
    window_average = sum(window) / window_size
    ch1rolling.append(window_average)

#create an array of length "window_size-1" to add to end of ch1rolling
    #so that the length of x and y are equal

addon = np.zeros(window_size-1) #create empty array of correct size (windowsize)
addon.fill(window_average) #fill that array with the last average from rolling ave
ch1rolling.extend(addon)


plt.plot(sqrtframe, ch1rolling, label= 'Channel 1 rolling')

#add labels and title to graphs

plt.legend()
plt.xlabel('square root of frame')
plt.ylabel('distance (pixels)')
plt.title('Flow profile of four channel microfluidic chip')
plt.show
   