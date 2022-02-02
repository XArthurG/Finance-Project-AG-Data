#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


import os
import pandas as pd

mydir = os.getcwd()

result = []
for file in os.listdir('Alphabet Inc (GOOG)/'):
    if file.endswith("-Alphabet.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0


# In[ ]:


length = len(sorted_list_0)

for i in range(length):
    
    if i == 0:
        file = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[i])

        size = len(file.index)
        size_1 = size - 1
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file
        
    else:
        file = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[i])
        size = len(file.index)
        size_1 = size - 1
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file_1.append(file)

file_1.drop(columns=file_1.columns[0], axis=1, inplace=True)
file_1.to_csv('Alphabet Inc (GOOG)/Alphabet-Ending-Months.csv', index=False)
#print(len(file_1))
#file_1


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Combined-Ratios.csv')
#print(len(file))

#new_header = file.iloc[0]
#file = file[1:]
#file.columns = new_header
print(len(file))

new_header = file.iloc[0]
file = file[1:]
file.columns = new_header

file


# In[ ]:


file_2 = file_1.reset_index()
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
#print(file_2)
numbers = file_2["Open"]
#file = file.join(numbers)
numbers_0 = numbers.squeeze()
#print(numbers)


# In[ ]:


file = file.reset_index()
file.drop(columns=file.columns[0], axis=1, inplace=True)
result = pd.concat([file, numbers_0], axis=1)

numbers = file_2["High"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Low"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Close"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Adj Close"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Volume"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)


# In[ ]:


result.to_csv('Alphabet Inc (GOOG)/2016-06-30-DF-Analysis.csv', index=False)


# In[ ]:


result.drop(columns=result.columns[0], axis=1, inplace=True)
result


# In[ ]:


from heading import *
from sklearn.linear_model import LinearRegression


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/2016-06-30-DF-Analysis.csv')
#print(file)
#file_0 = DataSet(name='2016-06-30-DF-Analysis', target='Close', attr_names='PE_1_VALUE PE_2_0_VALUE PE_2_1_VALUE EV_1_VALUE EV_2_VALUE EBIT_VALUE EBITDA_VALUE EV_1_EBITDA_VALUE EV_2_EBITDA_VALUE DE_VALUE QR_1_VALUE QR_2_VALUE EPS_VALUE DPS_VALUE DY_1_VALUE DY_2_VALUE Div_VALUE MCAP_VALUE ROE_VALUE NetMargin_VALUE OperatingMarging_VALUE Tax_VALUE FCF_0_VALUE FCF_1_VALUE FCF_2_VALUE RD_VALUE Open High Low Close AdjClose Volume')
file.drop(columns=file.columns[0], axis=1, inplace=True)

#train_data = []
#train_label = [] 
#test_data = []
#test_label = []


# In[ ]:


#file_0 = file.iloc[1: , :]
file_1 = file.reset_index()
file_1.drop(columns=file_1.columns[0], axis=1, inplace=True)
file_1


# In[ ]:


file_1.to_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None, index=False)
file_1.to_csv('aima-data/Dataset.csv', header=None, index=False)

#print(file)
#count = len(file)
#train_data, train_label, test_data, test_label = seperate_train_and_test_data(file, 1)
#file_0 = DataSet(name='2016-06-30-DF-Analysis', target='Close', attr_names='PE_1_VALUE PE_2_0_VALUE PE_2_1_VALUE EV_1_VALUE EV_2_VALUE EBIT_VALUE EBITDA_VALUE EV_1_EBITDA_VALUE EV_2_EBITDA_VALUE DE_VALUE QR_1_VALUE QR_2_VALUE EPS_VALUE DPS_VALUE DY_1_VALUE DY_2_VALUE Div_VALUE MCAP_VALUE ROE_VALUE NetMargin_VALUE OperatingMarging_VALUE Tax_VALUE FCF_0_VALUE FCF_1_VALUE FCF_2_VALUE RD_VALUE Open High Low Close AdjClose Volume')


# In[ ]:





# In[ ]:


#train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0, 1)


# In[ ]:


#dataTypeSeries = file_1.dtypes
#print('Data type of each column of Dataframe :')
#print(dataTypeSeries)

#print("\n")
#dataTypeObj = file_1.dtypes['PE_1_VALUE']
#print(dataTypeObj)

#file_1.astype({'PE_1_VALUE': 'int32'}).dtypes
#file_1['PE_1_VALUE'] = file_1['PE_1_VALUE'].astype(int)


# In[ ]:


#df = file_1['Close']
#df.to_frame()

#df.iloc[-2:-1] = 1092069.16882959
#df.iloc[-1:] = 1045588.00835278


# In[ ]:


## Had to manually remove the header (index number) on the left hand side [0-21] (label along y-axis)
# Try and do it using python
# FIXED :: file_1.to_csv(., index=False)

file_0 = DataSet(name='Dataset', target='Close', attr_names='PE_1_VALUE PE_2_0_VALUE PE_2_1_VALUE EV_1_VALUE EV_2_VALUE EBIT_VALUE EBITDA_VALUE EV_1_EBITDA_VALUE EV_2_EBITDA_VALUE DE_VALUE QR_1_VALUE QR_2_VALUE EPS_VALUE DPS_VALUE DY_1_VALUE DY_2_VALUE Div_VALUE MCAP_VALUE ROE_VALUE NetMargin_VALUE OperatingMarging_VALUE Tax_VALUE FCF_0_VALUE FCF_1_VALUE FCF_2_VALUE RD_VALUE Open High Low Close AdjClose Volume')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)


# In[ ]:


#@ TRY FOR VARIABLES WITH BEST-FIT, HIGH CORRELATION (EV_1, EBITDA, EPS... etc.)

file = pd.read_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None)

#file.drop(columns=file.columns[], axis=1, inplace=True)
#result = pd.concat([file, numbers_0], axis=1)


# DELETE COLUMNS UP TO 'Variable#1' e.g. EV_1_VALUE ##Index = 3
file.drop(file.iloc[:, 0:3], inplace = True, axis = 1)
# DELETE COLUMNS UP TO 'Close'
file.drop(file.iloc[:, 1:27], inplace = True, axis = 1)
file.drop(file.iloc[:, 2:], inplace = True, axis = 1)


file.to_csv('aima-data/Expected_Close_EV_1.csv', header=None, index=None)


# In[ ]:


file_0 = DataSet(name='Expected_Close_EV_1', target='Close', attr_names='EV_1_VALUE Close')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)
#df.to_csv('x_lr_predict_x.csv')


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None)

#file.drop(columns=file.columns[], axis=1, inplace=True)
#result = pd.concat([file, numbers_0], axis=1)


# DELETE COLUMNS UP TO 'Variable#1' e.g. EV_1_VALUE ##Index = 3 ##27-(x-3)
file.drop(file.iloc[:, 0:6], inplace = True, axis = 1)
# DELETE COLUMNS UP TO 'Close'
file.drop(file.iloc[:, 1:24], inplace = True, axis = 1)
file.drop(file.iloc[:, 2:], inplace = True, axis = 1)

file.to_csv('aima-data/Expected_Close_EBITDA.csv', header=None, index=None)

#file


# In[ ]:


file_0 = DataSet(name='Expected_Close_EBITDA', target='Close', attr_names='EBITDA_VALUE Close')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)
#df.to_csv('x_lr_predict_x.csv')


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None)

#file.drop(columns=file.columns[], axis=1, inplace=True)
#result = pd.concat([file, numbers_0], axis=1)


# DELETE COLUMNS UP TO 'Variable#1' e.g. EV_1_VALUE ##Index = 3 ##27-(x-3)
file.drop(file.iloc[:, 0:12], inplace = True, axis = 1)
# DELETE COLUMNS UP TO 'Close'
file.drop(file.iloc[:, 1:18], inplace = True, axis = 1)
file.drop(file.iloc[:, 2:], inplace = True, axis = 1)

file.to_csv('aima-data/Expected_Close_EPS.csv', header=None, index=None)

#file


# In[ ]:


file_0 = DataSet(name='Expected_Close_EPS', target='Close', attr_names='EPS_VALUE Close')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)
#df.to_csv('x_lr_predict_x.csv')


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None)

#file.drop(columns=file.columns[], axis=1, inplace=True)
#result = pd.concat([file, numbers_0], axis=1)


# DELETE COLUMNS UP TO 'Variable#1' e.g. EV_1_VALUE ##Index = 3 ##27-(x-3)
file.drop(file.iloc[:, 0:16], inplace = True, axis = 1)
# DELETE COLUMNS UP TO 'Close'
file.drop(file.iloc[:, 1:14], inplace = True, axis = 1)
file.drop(file.iloc[:, 2:], inplace = True, axis = 1)

file.to_csv('aima-data/Expected_Close_DIV.csv', header=None, index=None)

#file


# In[ ]:


file_0 = DataSet(name='Expected_Close_DIV', target='Close', attr_names='DIV_VALUE Close')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)
#df.to_csv('x_lr_predict_x.csv')


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Dataset.csv', header=None)

#file.drop(columns=file.columns[], axis=1, inplace=True)
#result = pd.concat([file, numbers_0], axis=1)


# DELETE COLUMNS UP TO 'Variable#1' e.g. EV_1_VALUE ##Index = 3 ##27-(x-3)
file.drop(file.iloc[:, 0:22], inplace = True, axis = 1)
# DELETE COLUMNS UP TO 'Close'
file.drop(file.iloc[:, 1:8], inplace = True, axis = 1)
file.drop(file.iloc[:, 2:], inplace = True, axis = 1)

file.to_csv('aima-data/Expected_Close_FCF_0.csv', header=None, index=None)

#file


# In[ ]:


file_0 = DataSet(name='Expected_Close_FCF_0', target='Close', attr_names='FCF_0_VALUE Close')
print(file_0.examples[0])
#print("\n")
print(file_0.examples[:3])
print("\n")

#

train_data = []
train_label = []
test_data = []
test_label = []

#

train_data, train_label, test_data, test_label = seperate_train_and_test_data(file_0.examples, 20)

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

#

lr = LinearRegression()
lr.fit(train_data,train_label)

#

train_accuracy= lr.score(train_data, train_label)
#print (train_accuracy)
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)
#print("\n")

#

for x in futureSample_data:
    print(x,lr.predict([x]))
    file_arr = x,lr.predict([x])
    
df = pd.DataFrame(file_arr)
#df.to_csv('x_lr_predict_x.csv')


# In[ ]:




