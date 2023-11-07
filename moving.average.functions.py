# building on moving.average.practice to create a moving average function to \
    #apply to all four channels and plot all four channels
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
plt.plot(sqrtframe, ch2, label= 'Channel 2')
plt.plot(sqrtframe, ch3, label= 'Channel 3')
plt.plot(sqrtframe, ch4, label= 'Channel 4')     

#add labels and title to graphs

plt.legend()
plt.xlabel('square root of frame')
plt.ylabel('distance (pixels)')
plt.title('Flow profile of four channel microfluidic chip')
plt.show

#now to create a function for applying a moving average

def rolling_average(channel_in, channel_out, window_size):
    window_size = 100 #how many points are being averaged together
    for i in range(len(channel_in) - window_size + 1):
        window = channel_in[i : i + window_size]
        window_average = sum(window) / window_size
        channel_out.append(window_average)
    
    #create an array of length "window_size-1" to add to end of ch1rolling
        #so that the length of x and y are equal
    
    addon = np.zeros(window_size-1) #create empty array of correct size (windowsize)
    addon.fill(window_average) #fill that array with the last average from rolling ave
    channel_out.extend(addon)
    plt.plot(sqrtframe, channel_out, label= 'Channel ? rolling')

#call rolling_average function to apply rolling average to all 4 channels
#I would like to further automate this
#I would like the names to be created automatically and for there to be \
    #no need to call "channel_out" because channel out is based on channel_in

window_size = 10
ch1rolling= []
rolling_average(ch1,ch1rolling, window_size)
ch2rolling= []
rolling_average(ch2,ch2rolling, window_size)
ch3rolling= []
rolling_average(ch3,ch3rolling, window_size)
ch4rolling= []
rolling_average(ch4,ch4rolling, window_size)

#add labels and title to graphs

plt.legend()
plt.xlabel('square root of frame')
plt.ylabel('distance (pixels)')
plt.title('Flow profile of four channel microfluidic chip')
plt.show
   