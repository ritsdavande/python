#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.array([10,20,30]) 
print(type(a)) 
print(a.shape)


# In[4]:


print(a[0], a[1], a[2])  
a[0] = 5   
print(a)   
b = np.array([[1,2,3],[4,5,6]])
print("dimension:=",b.shape)  


# In[5]:


print(b[0, 0], b[0, 1], b[1, 0])  
a = np.zeros((2,2))    
print(a)


# In[ ]:




