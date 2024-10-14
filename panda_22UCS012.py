#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#about Series


# In[1]:


import numpy as np;
import pandas as pd;


# In[2]:


data = np.array(['a','b','c','d'])


# In[3]:


s = pd.Series(data)
print(s);


# In[7]:


data1 = {'a' : 1.2 , 'b' : 1.3,'c' : 1.4}
s1 = pd.Series(data1)
print(s1);


# In[ ]:


#retriving the elements from series


# In[10]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[-3:])


# In[11]:


print(s[:-1])


# In[12]:


#Dataframe


# In[14]:


data = [['Parth',10],['Pratik',12],['Patil',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)


# In[15]:


data = {'Name':['Parth', 'Pratik', 'Patil', 'Ajinkya'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)


# In[20]:


d = {'one' : pd.Series(['a','b','c','d'],index=[1,2,3,4]),
      'two': pd.Series(['x','y','z'],index=[1,2,3])}
df = pd.DataFrame(d);
print(df)


# In[22]:


df['three']=pd.Series(['p','q','r'],index=[1,2,3])
print(df);


# In[ ]:





# In[ ]:




