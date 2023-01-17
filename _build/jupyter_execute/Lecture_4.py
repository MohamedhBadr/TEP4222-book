#!/usr/bin/env python
# coding: utf-8

# # Lecture 4 - Leontief Price Model
# Edgar Hertwich  
#   
# **Leontief Price Model**  
# In the following you import a global IO table, aggregated to 17 sectors of a single global economy. The steps necessary to parse this data and convert it to IO variables (in numpy) are already conducted.  
# We evaluate the following: what happens if all low-skilled workers receive a 50% raise? How much do prices of the different products increase? Which products are most affected? How much does the cost of household consumption increase?
# 

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_excel("IOweek4data.xlsx")
Zdf = df.iloc[0:17,3:20].set_index(df.iloc[0:17,0])
Ydf = df.iloc[0:17,21:27].set_index(df.iloc[0:17,0])
Vdf = df.iloc[18:25,3:20].set_index(df.iloc[18:25,1])
Fdf=df.iloc[40:43,3:20].set_index(pd.Series(['CO2','CH4','N2O']))
Vdf


# In[34]:


x = np.array(Zdf.sum(axis=1) + Ydf.fillna(0).sum(axis=1))


# In[40]:


A = np.array(Zdf) / x
S = np.array(Fdf) / x
V_bar = np.array(Vdf) / x
Y = np.array(Ydf)
L = np.linalg.inv(np.eye(17) - A)


# **Preparation**  
# What are the prices of the factors of production before the wage increase for low-skilled workers?  
# What are the prices of commodities before the increase in wages for low-skilled workers?  

# In[42]:





# **(a)** Define the price of factors of production, pi, after the increase in wages for low-skilled workers, assuming that there is no spillover to other groups.

# In[43]:


pi=np.array([1,1,1,1.5,1,1,1])


# **(b)** Calculate the price p of commodities after the wage rise for low-skilled workers. Display as a horizontal bar chart. 

# In[ ]:


p = pi @ V_bar @ L
p


# What are the two commodities that show the largest increase in prices? What does this tell us?
# 
# Write here: 

# **(c)** Calculate the increase in the average cost of living for households.

# In[47]:


CoLi = p @ Y[:,0] / sum(Y[:,0])


# In[48]:


CoLi


# In[ ]:




