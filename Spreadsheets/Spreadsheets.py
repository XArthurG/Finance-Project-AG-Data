#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!pip install pandas


# In[8]:


import pandas as pd
import os


# In[9]:


mydir = os.getcwd()

for file in os.listdir(mydir):
    if file.endswith(".xlsx"):
        print(os.path.join(file))


# In[10]:


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)      
    return allFiles


# In[11]:


dirName = mydir;
listOfFiles = sorted(getListOfFiles(dirName))
listOfFiles


# In[12]:


#del listOfFiles[0]
listOfFiles


# In[13]:


length = len(listOfFiles)

for i in range(length):
    input_date = listOfFiles[i]
    
    url = r'./' + input_date
    
    # s = pd.read_excel(url, sheet_name=1)
    # s_2 = pd.read_excel(url, sheet_name=3)
    # s_3 = pd.read_excel(url, sheet_name=6)
    
    s_3 = pd.read_excel(url, sheet_name=8)
    
    
    f_url = url.replace("./", "")
    ff_url = f_url.replace(".xlsx", "")

    #s.to_csv(ff_url + '-0.csv', index=False)
    #s_2.to_csv(ff_url + '-1.csv', index=False)
    s_3.to_csv(ff_url + '-2.csv', index=False)


# In[ ]:




