#!/usr/bin/env python
# coding: utf-8

# # Lecture 3 - Symmetric input-output table of the Norwegian economy  

# Edgar Hertwich, 2022
# 
# Data source: Nygård, Input-output analysis of the Norwegian economy, url={https://www.norges-bank.no/contentassets/c0a72b2d48084964a6804e09beb2d60b/staff_memo_2013_17.pdf}
# 
# The aim of this exercise is to  
#     - inspect a symmetric input-output table of Norway and thus learn some things about the Norwegian Economy  
#     - learn how to calculate and interpret the Leontief inverse  
#     - calculate the amount of imports to industries are required to satisfy the final demand by households, government, investment, and export.  
#     
#     

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_excel('NO_2010.xlsx',usecols='A:J', index_col=0)
df


# In[ ]:


Z = df.loc['Agriculture':'Finance','Agriculture':'Finance']
M = df.loc['Imports','Agriculture':'Finance']
V = df.loc['Labour':'Taxes','Agriculture':'Finance']


# **Q1: Define the matrices representing final demand (Y).**  
# - Evaluate the total demand by each final demand type and graph this.  

# In[ ]:





# **Q2: Market Balance.**  
# a) Calculate the total sales of each commodity. Display on a bar or pie chart. What is the most sold commodity?  
# b) Compare sales to industries (intermediate use) with sales to final demand. What share of commodities produced in Norway is also used as an input to production in Norway?  
# c) Who is the largest consumer of services? 

# In[ ]:


# a) Total sales of each commodity.

# The most sold commodity is: 


# In[ ]:


# b) intermediate vs final demand
Y_sum=Y.sum().sum()

#use the following code to print the share of intermediates:
#print('Of all commodities, {:.0%} are used as an input to production in Norway'.format(intermediate_share))


# In[ ]:


# c) largest consumer of services
all_sales=Z.join(Y)
all_sales.loc['Services'].plot(kind='bar')
# The largest consumer of services is the ...


# **Q3: Industry Balance.**  
# a) Calculate the total inputs to industry. Compare with answer to 2a). What do you notice?  
# b) How large is value added per unit output in each industry?   
# c) What industry has the highest capital intensity? What industry has the highest labor intensity?

# In[ ]:


# a) sum of inputs to industry

# Explain what you find: 


# **Q4: Input coefficients.**  
# 

# In[ ]:


V_bar=V.divide(x2)
M_bar = M.divide(x2)


# a) Calculate the A-matrix, i.e. the interindustry input coefficients. 

# In[ ]:





# b) what is the sum of all the input coefficients (interindustry, value added, imports) to an industry?

# In[ ]:





# c) What is the Leontief inverse of the A matrix? 

# In[ ]:


AA= np.array(A)
LL=np.linalg.inv(np.eye(5)-AA)
LL


# d) From the Leontief inverse, specify and graph the production volume required per unit output from the oil industry.  
# Where can I read this production volume?  
# I suggest converting the Leontief inverse np.array to a pandas data frame, that way you can plot in pandas and you have all the labels. You use the .iloc() method to identify the required data.

# In[ ]:


L=pd.DataFrame(LL, index=Z.index, columns=Z.columns)


# e) What are the imports required to norwegian industry to satisfy the four categories of final demand?

# In[ ]:


# write here the equation for Importsbydemand

pd.Series(data= Importsbydemand, index=Y.columns)


# In[ ]:




