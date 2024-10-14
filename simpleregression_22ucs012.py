#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[7]:


df=pd.read_csv("E:\ML_LAB_23\EXP2_Reg\\homeprices.csv")


# In[8]:


df


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')





# In[10]:


reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)



# In[11]:


reg.predict([[2400]])


# In[12]:


d=pd.read_csv("E:\ML_LAB_23\EXP2_Reg\\areas.csv")
d
reg.predict(d)


# In[ ]:




