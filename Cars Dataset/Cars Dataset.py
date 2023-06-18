#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


car = pd.read_csv(r"D:\Study Material\Data Analytics\Projects\Cars Dataset\2. Cars Data1.csv")


# In[ ]:


#Data Exploration


# In[8]:


car.head()


# In[9]:


car.shape


# In[10]:


#Data Cleaning


# In[11]:


#Find all the Null Values In The Dataset. If there is any null value in any column, then fil it with the mean of the column.


# In[16]:


car.isnull()


# In[14]:


car.isnull().sum()


# In[24]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace=True)


# In[25]:


car


# In[26]:


car.isnull()


# In[27]:


car.isnull().sum()


# In[28]:


#Check what are the different types of Make in the dataset. And what is the count (occurence) of each Make in the data?


# In[29]:


car.head(2)


# In[31]:


car['Make'].value_counts()


# In[32]:


#Filtering
#Show all the records where Origin is Asia or Europe.


# In[33]:


car.head(2)


# In[35]:


car[car['Origin'].isin(['Asia','Europe'])]


# In[36]:


#remove all the records (rows) where Weight is above 4000.


# In[37]:


car.head(2)


# In[40]:


car[~(car['Weight']> 4000)]


# In[42]:


428-99


# In[43]:


#Increase all the values of 'MPG_City' column by 3.


# In[44]:


car.head(2)


# In[46]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[47]:


car


# In[ ]:




