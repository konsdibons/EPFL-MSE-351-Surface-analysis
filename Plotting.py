#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:42:19 2023

@author: doruksinayuc
"""

import pandas as pd

# Replace 'your_file_path.xlsx' with the path to your Excel file
file_path = '/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Data/Surface_Analysis_Results.xlsx'

# Read the Excel file
df_firstSurvey = pd.read_excel(file_path, sheet_name='Initial Scan')
df_firstMultiplex = pd.read_excel(file_path, sheet_name='MultiplexInitialScan')
df_firstPointSputtering = pd.read_excel(file_path, sheet_name='Point1_Depth')
df_secondPointSputtering = pd.read_excel(file_path, sheet_name='Point2_Depth')
df_thirdPointSputtering = pd.read_excel(file_path, sheet_name='Point3_Depth')
df_finalScan = pd.read_excel(file_path, sheet_name='Final_Survey')

# Now, df is a DataFrame containing the contents of your Excel file

#%%
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file_path.xlsx' with the path to your Excel file
file_path = '/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Data/Surface_Analysis_Results.xlsx'

# Read the Excel file
df_firstSurvey = pd.read_excel(file_path, sheet_name='Initial Scan')
df_firstMultiplex = pd.read_excel(file_path, sheet_name='MultiplexInitialScan')
df_firstPointSputtering = pd.read_excel(file_path, sheet_name='Point1_Depth')
df_secondPointSputtering = pd.read_excel(file_path, sheet_name='Point2_Depth')
df_thirdPointSputtering = pd.read_excel(file_path, sheet_name='Point3_Depth')
df_finalScan = pd.read_excel(file_path, sheet_name='Final_Survey')

#%% FIRST SURVEY
# Plotting the bar graph with specified modifications
ax = df_firstSurvey.plot(kind='bar', edgecolor='black')
ax.set_ylabel("Composition")
ax.set_xticklabels(["Point 1", "Point 2", "Point 3"], rotation=0)  # Horizontal x-axis labels
ax.set_title("First Survey Scan")
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/FirstScan.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()
#%% FINAL SURVEY
# Plotting the bar graph with specified modifications
ax = df_finalScan.plot(kind='bar', edgecolor='black')
ax.set_ylabel("Composition")
ax.set_xticklabels(["Point 1", "Point 2", "Point 3"], rotation=0)  # Horizontal x-axis labels
ax.set_title("Final Survey Scan")
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/FinalScan.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()
#%% FIRST MULTIPLEX
# Plotting the bar graph with specified modifications
ax = df_firstMultiplex.plot(kind='bar', edgecolor='black')
ax.set_ylabel("Composition")
ax.set_xticklabels(["Point 1", "Point 2", "Point 3"], rotation=0)  # Horizontal x-axis labels
ax.set_title("Initial Multiplex")
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/FirstMultiplex.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()

#%% POINT 1 SPUTTERING
import numpy as np

# #Assuming sputter rate 1nm/min and take value every 30 seconds
# range_with_step = np.arange(0, 9.5, 0.5)

# Creating an array for the x-axis (0.5 nm steps)
nm_steps = [i * 0.5 for i in range(df_firstPointSputtering.shape[0])]

# Plotting the line graph 
plt.figure()
for column in df_firstPointSputtering.columns:
    plt.plot(nm_steps, df_firstPointSputtering[column], label=column)

plt.xlabel('Depth (nm)')
plt.ylabel('Composition')
plt.title('Depth Profile - Point 1')
plt.legend(loc='upper right')
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/FirstPointSputter.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()

#%% POINT 2 SPUTTERING
# Creating an array for the x-axis (0.5 nm steps)
nm_steps = [i * 0.5 for i in range(df_secondPointSputtering.shape[0])]

# Plotting the line graph 
plt.figure()
for column in df_secondPointSputtering.columns:
    plt.plot(nm_steps, df_secondPointSputtering[column], label=column)

plt.xlabel('Depth (nm)')
plt.ylabel('Composition')
plt.title('Depth Profile - Point 2')
plt.legend(loc='upper right')
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/SecondPointSputter.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()

#%% POINT 3 SPUTTERING
# Creating an array for the x-axis (0.5 nm steps)
nm_steps = [i * 0.5 for i in range(df_thirdPointSputtering.shape[0])]

# Plotting the line graph 
plt.figure()
for column in df_thirdPointSputtering.columns:
    plt.plot(nm_steps, df_thirdPointSputtering[column], label=column)

plt.xlabel('Depth (nm)')
plt.ylabel('Composition')
plt.title('Depth Profile - Point 3')
plt.legend(loc='upper right')
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/ThirdPointSputter.png', dpi=1200)  # Saves the figure as a PNG file with a DPI of 300
plt.show()

#%% STACKED PLOT FIRST POINT SPUTTERING
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named df_firstPointSputtering with your data
# nm_steps = [i * 0.5 for i in range(df_firstPointSputtering.shape[0])]

nm_steps = [i * 0.5 for i in range(df_firstPointSputtering.shape[0])]

# Prepare data for the stacked area plot
data_for_stackplot = []
for column in df_firstPointSputtering.columns:
    data_for_stackplot.append(df_firstPointSputtering[column])

# Creating a stacked area plot
plt.figure()
plt.stackplot(nm_steps, data_for_stackplot, labels=df_firstPointSputtering.columns)

plt.xlabel('Depth (nm)')
plt.ylabel('Composition')
plt.title('Depth Profile - Point 1 (Stacked Area Plot)')
plt.legend(loc='upper right')

# Save the figure
plt.savefig('/Users/doruksinayuc/OneDrive - metu.edu.tr/EPFL/Classes/Surface Analysis/Presentation/Figures/FirstPointSputter_V2.png', dpi=1200)  # Adjust the path and filename as needed

plt.show()



