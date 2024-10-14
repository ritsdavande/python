#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("E:\\ml\\EXP2_Reg\\homeprices.csv")


# In[4]:


df


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='blue',marker='*')


# In[6]:


# training the model


# In[7]:


reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)


# In[8]:


reg.predict([[3300]])


# In[9]:


reg.coef_


# In[10]:


reg.intercept_


# In[11]:


d=pd.read_csv("E:\\ml\\EXP2_Reg\\areas.csv")


# In[12]:


d


# In[13]:


d.head(4)


# In[14]:


reg.predict(d)


# In[15]:


p = reg.predict(d)


# In[16]:


d['price']=p


# In[17]:


d.to_csv("E:\\prediction.csv")


# In[ ]:




