# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 13:17:30 2023

@author: Aswini
"""

import pandas as pd #Importing pandas for analysis
import matplotlib.pyplot as plt #Importing matplotlib for Data Visualisation

df = pd.read_csv("Assignmentfuel.csv", index_col=0) #Load data from CSV file

#Generates line plot for fuel export data
def fuel_linePlot(linePlotData):
    plt.figure() #Create new figure for line plot
    
    '''Plotting the data where X axis is years and y axis is export rate of countries, 
    Defining type of plot as line plot with figure size and marker style 
    for clear data points, adding title and x,y labels.'''
    
    linePlotData.plot(x='Years', y=['Bahrain', 'Kuwait', 'Malta', 'Oman', 
                                    'Qatar','Saudi Arabia', 
                                    'United Arab Emirates'],
                      kind='line', figsize=(11, 5), marker='o') 
    plt.title('Maximum % of Fuel Exports') 
    plt.xlabel('Years') 
    plt.ylabel('Export rate')
    plt.legend() 
    plt.show() 

#Generates barplot for fuel export data
def fuel_barPlot(barData):
    
    '''Plotting a bar plot to compare fuel export of UAE and Kuwait
    where X axis represents years and y axis is export rate of two countries,
    setting the title and labelling x and y and Setting the colors for the bars for better visualization''' 

    barData.plot(x='Years', y=['United Arab Emirates', 'Kuwait'], kind='bar', title=' United Arab Emirates vs Kuwait fuel export', 
                 xlabel='Years', ylabel='Fuel Export', color=('purple', 'green'), legend=True, width=0.65) 
    plt.figure(figsize=(11, 5)) # Creates ne figure and setting the size.
    plt.show() 

#Generates barplot for fuel export data
def fuel_scatterPlot(scatterData):
    plt.figure(figsize=(11, 5))
    
    '''Plotting a scatter plot to compare fuel export of Malta and Bahrain
    where X axis represents years and y axis is export rate of two countries,
    setting the title and labelling x and y and legend is set to upper right for better visualization'''
    
    plt.scatter(scatterData['Years'], scatterData['Malta'], label='Malta')
    plt.scatter(scatterData['Years'], scatterData['Bahrain'], label='Bahrain')
    plt.title('Malta vs Bahrain Fuel Exports')
    plt.xlabel('Years')
    plt.ylabel('Export rate')
    plt.legend(loc='upper right')
    plt.show()


#Removing the last 5 nugatory rows
df = df.iloc[:-5]

#Droping the unwanted columns from the dataset
df1 = df.drop(['Country Code', 'Series Name', 'Series Code'], axis=1)

#Transpoing the dataframe to access the country as column variable:
df1_trans = df1.transpose()
df1_trans.head()

# Resetting the index of DataFrame df1_trans and creating a new DataFrame df2
df2 = df1_trans.reset_index(drop=True)
df2.head()

#Adding a column of 'Years' to the dataframe
year = pd.Series([2013, 2014, 2015, 2016, 2017, 2018,
                 2019, 2020, 2021], dtype=object)
df2['Years'] = year
df2.head()

# df_final is a new DataFrame where the last column is moved to the first one
df_final = pd.concat([df2.iloc[:, -1:], df2.iloc[:, :-1]], axis=1)
df_final.head()

#Function generating a line plot using data frame df_final
fuel_linePlot(df_final)

#Function generating a Bar plot using data frame df_final
fuel_barPlot(df_final)

#Function generating a Scatter plot using data frame df_final
fuel_scatterPlot(df_final)
