#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_csv(r"D:\Study Material\Data Analytics\Projects\India Census 2011\6. India Census 2011.csv")


# In[4]:


data


# In[5]:


#Data Exploration


# In[6]:


#How will you hide the indexes of the dataframe?


# In[7]:


data.style.hide_index()


# In[8]:


#How can we set the caption/heading on the dataframe?


# In[9]:


data.head(2)


# In[10]:


data.style.set_caption("India Census 2011 Dataset")


# In[11]:


#Show the records related with the districts - New Delhi, Lucknow, Jaipur.


# In[12]:


data[data['District_name'].isin(['New Delhi','Lucknow','Jaipur'])]


# In[14]:


#Calculate State-wise: 
#1. Total Number of Population 


# In[15]:


data.head(1)


# In[18]:


data.groupby('State_name').Population.sum().sort_values(ascending =False)


# In[19]:


#2. Total Number of Population for different religions


# In[20]:


data.head(1)


# In[21]:


data.columns


# In[25]:


data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values('Christians')


# In[27]:


#How many male workers are there in Maharashtra?


# In[29]:


data[data.State_name=='MAHARASHTRA']['Male_Workers'].sum()


# In[30]:


#How to set a column as the index of the dataframe?


# In[32]:


data.set_index('District_code')


# In[33]:


#Add a suffix to the column names.


# In[34]:


data=data.add_suffix('_rightone')


# In[35]:


data


# In[36]:


#Add a prefix to the column names.


# In[39]:


data.add_prefix('leftone_')


# In[ ]:




