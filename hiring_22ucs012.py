#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn import linear_model


# In[2]:


df=pd.read_csv("E:\ML_LAB_23\Exp 3 linera_regression_multivariate\\hiring.csv")


# In[3]:


df


# In[6]:


reg=linear_model.LinearRegression()
reg.fit(df[['experience','test_score','interview_score']],df.salary)


# In[7]:


reg.predict([[15,9,8]])


# In[8]:


reg.coef_


# In[9]:


reg.intercept_


# In[10]:


reg.predict([[1,5,5]])


# In[ ]:




