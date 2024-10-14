#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import linear_model
import matplotlib as plt


# In[7]:


df=pd. read_csv("E:\ML_LAB_23\Exp 3 linera_regression_multivariate\\homeprices.csv")


# In[8]:


df


# In[10]:


reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)


# In[11]:


reg.predict([[3000,3,15]])


# In[12]:


reg.coef_


# In[13]:


reg.intercept_


# In[ ]:




