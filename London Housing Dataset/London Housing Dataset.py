#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[85]:


data = pd.read_csv(r"D:\Study Material\Data Analytics\Projects\London Housing Dataset\5. London Housing Data.csv")


# In[86]:


data


# In[87]:


#Data Exploration


# In[88]:


data.count()


# In[89]:


data.isnull().sum()


# In[90]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[91]:


sns.heatmap(data.isnull())


# In[92]:


#Convert the Datatype of 'Date' column to Date-Time Format.


# In[93]:


data.head()


# In[94]:


data.dtypes


# In[95]:


data.date= pd.to_datetime(data.date)


# In[96]:


data.dtypes


# In[97]:


#Add a new column 'Year' in the dataframe, which contains years only.


# In[98]:


data.head()


# In[99]:


data["year"]=data.date.dt.year


# In[100]:


data


# In[101]:


#Add a new column 'Month' as 2nd column in the dataframe, which contains month only.


# In[102]:


data.insert(1,'month',data.date.dt.month)


# In[103]:


data


# In[104]:


#Remove the columns 'Year' and 'Month' from the dataframe.


# In[108]:


data.drop(['month','year'], axis=1, inplace=True)


# In[109]:


data.head()


# In[110]:


#Show all the records where 'No. of Crimes' is 0. And, how many such records are there? 


# In[111]:


data.head()


# In[116]:


len(data[data.no_of_crimes ==0])


# In[117]:


#What is the maximum and minimum 'average_price' per year in England?


# In[118]:


data['year'] =data.date.dt.year


# In[120]:


data.head()


# In[122]:


df1=data[data.area=='england']
df1


# In[123]:


df1.groupby('year').average_price.max()


# In[124]:


df1.groupby('year').average_price.min()


# In[125]:


#What is the Maximum and Minimum No. of Crimes recorded per area?


# In[129]:


data.groupby('area').no_of_crimes.max().sort_values(ascending=True)


# In[128]:


data.groupby('area').no_of_crimes.min().sort_values(ascending=True)


# In[130]:


#Show the total number of records of each area, where average price is less than 100000.


# In[133]:


data[data.average_price<100000].area.value_counts()


# In[ ]:




