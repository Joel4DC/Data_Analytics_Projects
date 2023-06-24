#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


data= pd.read_csv(r"D:\Study Material\Data Analytics\Projects\COVID-19 Dataset\4. covid_19_data.csv")


# In[15]:


data


# In[16]:


#Data Exploration


# In[17]:


data.count()


# In[18]:


data.isnull()


# In[19]:


data.isnull().sum()


# In[20]:


import seaborn as sns


# In[21]:


import matplotlib.pyplot as plt


# In[22]:


sns.heatmap(data.isnull())


# In[23]:


#Data Analytics


# In[24]:


#Show the number of Confirmed, Deaths and Recovered cases in each Region.


# In[25]:


data.head(2)


# In[26]:


data.groupby('Region').sum().head(20)


# In[27]:


#Show the number of Confirmed cases in each Region.


# In[28]:


data.groupby('Region')['Confirmed'].sum().head(20)


# In[32]:


data


# In[30]:


#Remove all the records where Confirmed Cases is Less Than 10. 


# In[31]:


data.head(2)


# In[35]:


data = data[~(data.Confirmed<10)]


# In[36]:


data


# In[39]:


data.head(20)


# In[40]:


#In which Region, maximum number of Deaths cases were recorded?


# In[48]:


data.groupby('Region').Confirmed.sum().sort_values(ascending =False).head(20)


# In[49]:


#In which region, minimum number of Deaths were recorded?


# In[50]:


data.head()


# In[53]:


data.groupby('Region').Deaths.sum().sort_values(ascending =True).head(50)


# In[54]:


#How many Confirmed, Deaths and Recovered cases were reported from India till 29th April 2020?


# In[55]:


data.head()


# In[56]:


data[data.Region =='India']


# In[57]:


#How many Confirmed, Deaths and Recovered cases were reported from USA till 29th April 2020?


# In[59]:


data[data.Region=='US']


# In[60]:


# Sort the entire data wrt No. of Confirmed cases in ascending order.


# In[61]:


data.head(2)


# In[62]:


data.sort_values(by =['Confirmed'], ascending =True).head(20)


# In[63]:


#Sort the entire data wrt No. of Recovered cases in descending order.


# In[67]:


data.sort_values(by= ['Recovered'], ascending = False)


# In[ ]:




