#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install pandas


# In[2]:


import pandas as pd


# In[3]:


#excel_file = pd.read_excel('./2016-06-30.xlsx')
#excel_file.head()

#excel_file = pd.read_excel('./2016-06-30.xlsx', sheet_name = 6)
#excel_file.head()


# In[4]:


input_date = input()


# In[5]:


url = r'./' + input_date + '.xlsx'


# In[6]:


s = pd.read_excel(url, sheet_name=1)
#s_2 = pd.read_excel(url, sheet_name=3)
#s_3 = pd.read_excel(url, sheet_name=6)


# In[7]:


f_url = url.replace("./", "")
ff_url = f_url.replace(".xlsx", "")


# In[8]:


#s


# In[9]:


#s_2


# In[10]:


#s_3


# In[11]:


s.to_csv(ff_url + '-0.csv', index=False)
#s_2.to_csv(ff_url + '-1.csv', index=False)
#s_3.to_csv(ff_url + '-2.csv', index=False)


# In[ ]:




