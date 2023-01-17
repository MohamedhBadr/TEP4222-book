#!/usr/bin/env python
# coding: utf-8

# # Problem set 3 - Symmetric input-output tables

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt


# In[2]:


#import your data
df = pd.read_excel (r'IOweek3data.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df


# In[70]:


#Define Z (Interindustry Matrix)
Z = df.iloc[1:18] # first select relevant rows
Z = Z.iloc[:, 0:21] # select relevant columns
Z = Z.drop(df.columns[[1, 2, 3]], axis=1) #drop irrelevant columns
Z = Z.set_index('Unnamed: 0') #reset index
Z


# In[71]:


#define final demand table
Y = df.iloc[1:18] # first select relevant rows
Y = Y.iloc[:, 22:29] # select relevant columns
Y


# In[72]:


#define Value added table
V = df.iloc[19:45] # first select relevant rows
V = V.iloc[:, 0:21] # select relevant columns
V = V.drop(df.columns[[2, 3]], axis=1) #drop irrelevant columns
V = V.set_index('Unnamed: 1') #reset index
V = V.drop(labels=['Unnamed: 0'], axis=1)
V


# In[73]:


#define enviornmental extention matrix
F = df.iloc[45:1352] # first select relevant rows
F = F.iloc[:, 0:21] # select relevant columns
F = F.drop(df.columns[[2, 3]], axis=1) #drop irrelevant columns
F = F.set_index('Unnamed: 1') #reset index
F = F.drop(labels=['Unnamed: 0'], axis=1)
F


# In[84]:


#Create on table with Z and Y Intermediate trade and final demand
Z_Y = df.iloc[1:18] # first select relevant rows
Z_Y = Z_Y.iloc[:, 0:29] # select relevant columns

#Get total output X
Z_Y["Total_output"] = Z_Y.sum(axis=1)
X = Z_Y["Total_output"] 

#adjust X and create A (interindustry technical coefficients)
X = X.tolist()
X
A = Z/X
A


# In[24]:


#Create one table with Intermediate and Value added together to get total output
Z_V = pd.concat([Z, V])
Z_V.loc['Total_Output']= Z_V.sum()
Z_V


# In[85]:


#get technical coefficients for Value added table 
T_V = V/X
T_V


# In[86]:


#Get technical coefficients for enviornmental extensions table 
S = F/X
S


# What was the per capita expenditure for electricity, gas and water, given that we were ca.7 billion people on the planet in 2011? 
# 

# In[68]:


#Get Final consumer demand expenditure by houshold for electricity water and gas 
#and then divide it by 7000 (remember that these numbers are in millions)

#Select 11th row in matrix Y
Final_household = Y.iloc[10]
Final_household = Final_household["Final consumption expenditure by households"]
Popullation = 7000 #in millions

#Calculate expenditure per capita by deviding on 7000 
PerCaptia = Final_household/Popullation
PerCaptia


# What were the CO2 emissions from combustion per unit output from each of the sectors? What sector did have the highest expenditure for electricity, gas and water per unit output? 

# In[87]:


#Create a Data frame with total emissions by industry by unit of output

#Now that we have the technical coefficient matrix all we need to do is locate the row of C02 emirriosn from combustion 
#In the S matrix (coefficients for enviornmental extensions)
Array = S.loc['CO2 - combustion - air']
Array


# In[88]:


Array.plot(kind='bar')


# Calculate the carbon footprint of all products in final consumption. Develop a figure that shows the total carbon footprint for all the 17 products, i.e. per product.

# In[89]:


#since we are looking for the total figure and not the per unit figure we will look in the F matrix

#Start of by creating a Total row 
F.loc['Carbon_Footprint']= F.sum()

#Then we can plot this row
F.loc['Carbon_Footprint'].plot(kind='bar')


# What was the carbon footprint of different final consumers, i.e. different columns in the Y matrix? 

# In[90]:


#we will look in the Y matrix

#Start of by creating a Total row 
Y.loc['Carbon_Footprint']= Y.sum()

#Then we can plot this row
Y.loc['Carbon_Footprint'].plot(kind='bar')

