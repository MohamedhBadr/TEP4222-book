#!/usr/bin/env python
# coding: utf-8

# # Problem Set 2 - The Industry and Final Demand Balances

#     
# The Firm Balance expresses the balance between revenue for products supplied by an industry and the expenditure for the intermediate inputs and factors of production. We would like to test this balance looking at the supply and use tables for the United States in 2021. 
#     
# A second balance of sorts is between value added and final demand. Value added can be interpreted as income of households and governments, while final demand is the expenditure of households and government. Measured in the same valuation and in a closed economy, these should balance. The second analysis we will conduct is to investigate income and expenditure of households and government.
#     
# Please conduct this exercise using matrix algebra in numpy. For summation, use vectors of 1. 
#     

# <b>Your name: </b> 

# In[1]:



# US Supply and Use Tables from url = "https://www.bea.gov/industry/input-output-accounts-data"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:



Use_raw = pd.read_csv("data/U15_US_2021.csv", header=3, index_col=1, na_values='---').drop('Unnamed: 0', axis=1)   
Use=Use_raw.iloc[0:17,0:15].fillna(0) 
ValueAdded=Use_raw.iloc[18:22,0:15].fillna(0) 
FinalDemand=Use_raw.iloc[0:17,16:21].fillna(0)

Supply_raw = pd.read_csv(r'data/S15_US_2021.csv', header=3, index_col=1,na_values='---')
Supply=Supply_raw.iloc[0:17,1:16].fillna(0) 


# Please feel free to explore the dataframes that we created to ensure that they contain the information we want.
# 
# We now create a new dataframe that store the results of our calculations per industry. Which of those matrices had a dimension industry? 

# In[3]:


IndustrySums = pd.DataFrame(index=sum_expenditure.index, 
    columns = ['Revenue','Intermediate Inputs', 'Production Factors','Total Expenditure', 'Rev/exp ratio'])


# In order to do sums in the proper way in linear algebra, we need vectors of 1. In addition, we need to know that the multiplication of two matrices is represented in numpy by the '@' symbol. 

# <b>Q1.</b> What is the total revenue per industry sector? Calculate this using a matrix multiplication. 

# In[ ]:


#Define the number of commodities and create a vector of that size
n_commodities = Supply.shape[0]
i_c = np.ones(n_commodities)
IndustrySums['Revenue'] = Supply.T @ i_c


# <b>Q2.</b> What is the cost of intermediate inputs per industry? Calculate as above.

# In[ ]:


#Please remove comment sign (#) and complete equation below
#IndustrySums['Intermediate inputs'] =  @
IndustrySums


# <b>Q3.</b> What is the value addded per industry? What is the total expenditure per industry?

# In[ ]:


i_w = np.ones(ValueAdded.shape[0])
#IndustrySums['Value Added'] = 
#IndustrySums['Total Expenditure'] = 
IndustrySums['Rev/exp ratio'] = IndustrySums['Revenue']/IndustrySums['Total Expenditure']
IndustrySums


# <b>Q4.</b> Graph the results, comparing revenue and total expenditure, on a scatter plot (x-y chart).

# In[ ]:


i_i = np.ones(Use.shape[1])
i_e = np.ones(FinalDemand.shape[1])


# <b>Q5.</b> How close are revenue and total expenditure? Is there an explanation for the difference?

# Write your answer here.
# 
# 
# 
# 

# <b>Q6.</b> Sum the components of value added across industries. What is the share of income of governments and households contributed by each of the components of value added. Display using a pie or bar chart. 

# In[ ]:


i_i = np.ones(Use.shape[1])
#SumValueAdded = @


# <b>Q7.</b> What is the final demand by final demand category? Who spends the money in the United States? What is the fraction of total final demand constituted by government expenditure? 

# In[ ]:


#SumFinalDemand = i_c.T @ FinalDemand

SumFinalDemand.plot.barh(xlabel = 'Million $', title = 'Final Demand 2021')


# <b>Q8.</b> Compare the sum totals of final demand and value added. Why do you think they are different?

# In[ ]:





# In[ ]:





# <b>Q9.</b> Compare Gross operating surplus and private fixed investment. What fraction of surplus is being reinvested? 

# In[ ]:





# In[ ]:




