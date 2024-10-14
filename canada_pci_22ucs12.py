#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn import linear_model
 


# In[16]:


df=pd.read_csv("E:\ML_LAB_23\Exp 3 linera_regression_multivariate\\pci.csv")


# In[17]:


df


# In[18]:


reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.pci)



# In[21]:


reg.predict([[2020]])


# In[22]:


reg.coef_


# In[23]:


reg.intercept_


# In[ ]:




