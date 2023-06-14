#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"D:\Study Material\Data Science\Projects\1. Weather Data.csv")


# In[3]:


data


# In[ ]:


#Data Exploration


# In[4]:


data.head()


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[13]:


data['Weather'].unique


# In[15]:


data['Weather'].unique()


# In[16]:


data['Weather'].nunique()


# In[17]:


data.nunique()


# In[19]:


data.count()


# In[20]:


data['Weather'].value_counts()


# In[21]:


data.info()


# In[22]:


#Data Analytics


# In[23]:


#Find all the unique 'Wind Speed' values in the data.


# In[25]:


data.head(2)


# In[27]:


data.nunique()


# In[29]:


data['Wind Speed_km/h'].nunique()


# In[31]:


data['Wind Speed_km/h'].unique()


# In[32]:


#Answer= 34


# In[33]:


#Find the number of times when the 'Weather is exactly Clear'.


# In[34]:


data.head(2)


# In[35]:


#value counts
data.Weather.value_counts()


# In[37]:


#Filtering
data[data.Weather == 'Clear']


# In[38]:


#groupby
data.groupby('Weather').get_group('Clear')


# In[39]:


#Answer= 1326 times


# In[40]:


#Find the number of times when the 'Wind Speed was exactly 4km/h'.


# In[41]:


data.head(2)


# In[43]:


data[data['Wind Speed_km/h']== 4]


# In[44]:


#Answer= 474 times


# In[45]:


#Find out the Null values in the data.


# In[46]:


data.isnull().sum()


# In[48]:


data.notnull().sum()


# In[49]:


#Answer= 0


# In[50]:


#Rename the column name 'Weather' of the dataframe to 'Weather Condition'.


# In[51]:


data.head(2)


# In[52]:


#temporary
data.rename(columns = {'Weather': 'Weather Condition'})


# In[53]:


#permanent
data.rename(columns ={'Weather':'Weather Condition'}, inplace =True)


# In[54]:


data.head()


# In[55]:


#What is the mean of 'Visibility'.


# In[56]:


data.head(2)


# In[57]:


data.Visibility_km.mean()


# In[58]:


#Answer=27.664446721311478


# In[59]:


#What is the standard deviation of "Pressure" in this Data?


# In[60]:


data.Press_kPa.std()


# In[61]:


#Answer= 0.8440047459486474


# In[62]:


#What is the variance of 'Relative Humidity' in this Data?


# In[63]:


data['Rel Hum_%'].var()


# In[64]:


#Answer= 286.2485501984998


# In[66]:


#Find all the instances when 'Snow' was recorded.


# In[68]:


data.head(2)


# In[69]:


#value counts
data['Weather Condition'].value_counts()


# In[77]:


#Filtering
data[data ['Weather Condition']=='Snow']


# In[80]:


#Answer 'Only Snow'= 390 


# In[79]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[81]:


#Answer 'Snow as a string'= 583


# In[82]:


#Find out all the instances when 'Wind Speed is above 24' and Visibility is 25'.


# In[83]:


data.head(2)


# In[92]:


data[(data['Wind Speed_km/h']> 24) & (data['Visibility_km'] == 25)]


# In[95]:


#Answer= 308


# In[ ]:


#What is the Mean Value of each column against each 'Weather Condition'?


# In[94]:


data.head()


# In[96]:


data.groupby('Weather Condition').mean()


# In[97]:


#Answer= Given Above


# In[98]:


#What is the minimum and maximum value of each column against each 'Weather Condition'?


# In[99]:


data.head(2)


# In[100]:


data.groupby("Weather Condition").min()


# In[101]:


data.groupby("Weather Condition").max()


# In[102]:


#Answer= Given Above


# In[103]:


#Show all the Records where Weather Condition is Fog.


# In[104]:


data[data['Weather Condition']=='Fog']


# In[105]:


#Answer= 150 times


# In[106]:


#Find all the instances when 'Weather is Clear' or 'Visibility is above 40'.


# In[107]:


data[(data["Weather Condition"]=='Clear') | (data['Visibility_km']>40)]


# In[108]:


#Answer= 3027


# In[109]:


#Find all instances when:
#'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'.


# In[117]:


data.head(2)


# In[120]:


data[(data['Weather Condition']=='Clear')& (data['Rel Hum_%']>50)| (data['Visibility_km']> 40)]


# In[121]:


#Answer= 2921


# In[ ]:




