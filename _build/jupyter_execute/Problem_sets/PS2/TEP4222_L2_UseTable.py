#!/usr/bin/env python
# coding: utf-8

# <b>TEP4222 2023 Exercise Lecture 2 - Exploratory Data Analysis of the Use Table  
#     
# Last week, we looked at the Supply Table for the US. Online, you find a Jupyter Notebook which imports the Supply Table, parses it (i.e., creates a variable that describes the part of the downloaded data that is of interest), and performs the sums to anser the questions. Please make sure you understand these operations. 
#     
# In the first part of the present exercise, we import the US Use Table and prepare it for subsequent analysis by separating out relevant, distinct parts (parsing). Then we do some exploratory data analysis to get to know the use table. 
# 
# Like the supply table, the published use table comes with various sums of columns and rows. We are only interested in the primary data; python can do summations and so we do not need to have the data summed. Further, the use table has  distinct blocks: <br> 
#     - the use of commodities as intermediate input by industries,  
#     - the use of factors of production (components of value added) by these industries, and  
#     - the use of commodities by final demand, which includes final consumption by households, non-governmental institutions serving households, the government, as well as export, investment, and storage.  
#     We identify those block and form the tables Use, Value Added, and FinalDemand. _Examine these tables and identify large flows_.<br><br> 
#     <i>Q1: What is the sum total of each of those three matrices?</i><br>
#     <i>Q2: Determine and plot the total operating surplus of each industry sector.</i> What can we conclude from this? Why do you think it is called total operating surplus? What do costs do you think this surplus needs to cover? How is it different from profit?  
#     _Q3: Plot the compensation of employees_. How does the sector distribution differ from that of the surplus?  
# _Q4: Determine and plot the share of operating surplus in the value added in each sector._  
#     _Q5: What industries are using agricultural products as intermediate inputs? Make a plot._  
#     _Q6: Calculate the input coefficients (inputs per unit industry turnover). What commodities are used by all industries?_  
#     _Q7: Compare the demand for commodities by industry with the final demand._ Which commodities are primarily used by industries? Which are predominantly used by final consumers?
#     

# In[1]:



# US Supply and Use Tables from url = "https://www.bea.gov/industry/input-output-accounts-data"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

UseTable = pd.read_csv("U15_US_2021.csv", header=3, index_col=1, na_values='---').drop('Unnamed: 0', axis=1)   
        #You may have to add a path to the file name


# In[12]:


UseTable


# Examine the sections of the table by checking the row and column names. If this does not show well on your PC, do so in the Excel version of the table. (PS: Please note that the drop command below just serves to delete the column of sector numbers).

# Define the intermediate use (by industries) of commodites. The second line defines the number of digit after the comma. fillna(0) replaced Nan by zero. The last command formats the background of the table in colors depending on the size of the value. Please examine these tables.

# In[20]:


Use=UseTable.iloc[0:16,1:15]             #Use of commodities by industries
pd.set_option('display.precision', 0)
Use.fillna(0).style.background_gradient(cmap ='Blues')


# In[21]:


ValueAdded=UseTable.iloc[18:21,1:15]                     #Use of Factors of Production by industry
ValueAdded.style.background_gradient(cmap ='Blues')


# In[24]:


FinalDemand=UseTable.iloc[0:16,17:22]
#Have a look at the table. Identify the largest final demand category for each commodity. (Just note, no need to report.)


# **Q1: What is the sum total of those three matrices?**  
# Please also print out the total volume of value added and final demand. The Use table is in million US dollars. 

# In[ ]:


Use_Total = Use.sum().sum()

print('Total use of commodities by industries:', Use_Total/1000000, ' trillion dollars')
# print the sums in trillions for the two other matrices. Why did we have to sum twice?


# In[ ]:


#How do you like this figure? Why do we need to sum only once? What happens if we write (axis=1) after sum?
ValueAdded.sum().plot(kind='pie')


# **Q2: Determine and plot the total operating surplus of each industry sector.**

# In[ ]:


(ValueAdded/1000).loc['Gross operating surplus'].plot(kind='hbar',xlabel='Surplus in billion $')


# **Q3: Determine and plot the compensation of employees.**

# In[ ]:





# **Q4: Determine and plot the share of operating surplus in the value added in each sector.**

# In[ ]:


SurplusShareVA=ValueAdded.loc['Gross operating surplus']/ValueAdded.sum()
SurplusShareVA.plot(kind='bar', ylabel="Surplus per unit Value Added")


# **Q5: What industries are using agricultural products as intermediate inputs? Make a plot.**

# In[ ]:





# **Q6: Calculate the input coefficients (inputs per unit industry turnover).** What commodities are used by all industries?

# In[ ]:


IndustryTotalInput = Use.sum() + ValueAdded.sum()
IndustryTotalInput.plot(kind='pie')


# In[ ]:


##Fill in here:
Use_coefficient # = ...
pd.set_option('display.precision', 2)
Use_coefficient.fillna(0).style.background_gradient(cmap ='Blues')


# In[ ]:


print('Following commodities are used by all industries: (fill in here)')


# **Q7: Compare the demand for commodities by industry with the final demand.**     
# Which commodities are primarily used by industries? Which are predominantly used by final consumers?

# In[ ]:


df1=pd.DataFrame(data=Use.sum(axis=1), columns=['Intermediate'])
df2=pd.DataFrame(data=FinalDemand.sum(axis=1), columns=['Final'])
CommodityDemand=df1.merge(df2, on='Name')
(CommodityDemand/1000000).plot(kind='bar',stacked=True, ylabel='Commodity demand trillion $')


# In[ ]:


CommodityDemand.sum().plot(kind='pie')


# In[ ]:


CommodityDemand.plot(kind='scatter', x='Intermediate', y='Final')


# Write your interpretation of the results in Q7 here:

# In[ ]:




