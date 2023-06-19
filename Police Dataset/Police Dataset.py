#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data =pd.read_csv(r"D:\Study Material\Data Analytics\Projects\Police Dataset\3. Police Data.csv")


# In[4]:


data.head()


# In[5]:


#Data Exploration


# In[6]:


#Data Cleaning


# In[9]:


#Remove the columns containing the missing values


# In[8]:


data.isnull().sum()


# In[13]:


data.drop(columns='country_name',inplace=True)


# In[14]:


data


# In[15]:


#For Speeding, were Men or Women stopped more often?


# In[16]:


data.head()


# In[17]:


data[data.violation =="Speeding"].driver_gender.value_counts()


# In[18]:


#Does gender affect who gets searched during a stop?


# In[20]:


data.groupby('driver_gender').search_conducted.sum()


# In[21]:


data.search_conducted.value_counts()


# In[22]:


#What is the Mean stop duration?


# In[25]:


data.head()


# In[26]:


data.stop_duration.value_counts()


# In[37]:


data['stop_duration']= data['stop_duration'].map({'0-15 Min': 7.5, '16-30 Min': 24, '30+ Min':45})


# In[38]:


data


# In[39]:


data['stop_duration'].mean()


# In[40]:


#Compare the age distributions for each violation


# In[41]:


data.head()


# In[47]:


data.groupby('violation').driver_age.describe()


# In[ ]:




