#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')


# In[5]:


df.head()


# In[7]:


df.tail()


# In[6]:


region_df.head()


# In[8]:


df.info()


# In[9]:


df.shape


# In[17]:


df=df[df['Season']=='Summer']


# In[16]:


df


# In[18]:


df.shape


# In[21]:


#merging the two dataframes 
# Explanation:
# df: The main dataset containing Olympic athlete data.
# region_df: A dataset that likely contains region or country information mapped to NOC codes.
# on='NOC': Merges both dataframes using the 'NOC' column as the common key.
# how='left': Ensures all rows from df remain, even if there is no matching row in region_df (missing values will be NaN).
df=df.merge(region_df,on='NOC', how = 'left')


# In[22]:


df


# In[32]:


df['Region'].unique()


# In[23]:


print(region_df.columns)  # Ensure 'region' exists in region_df


# In[24]:


df.isnull().sum()


# In[30]:


df.drop_duplicates(inplace =True)


# In[29]:


df.duplicated().sum()


# In[33]:


df['Medal'].value_counts()


# In[34]:


df['Year'].value_counts()


# In[36]:


#one hot encoding of medals
pd.get_dummies(df['Medal'])


# In[41]:


#cancatenting the one-hot encoded medals data to original dataframe
df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)


# In[42]:


df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()


# In[43]:


#here you can see the total gold medal won by india is 131 as 
# shown in below count but in actual only 9 or 10 gold medal has won by india
# so in the dataset there is an error regarding countin
# of medals (if one team has won the medal the whole membrer 
# is counted as every member 
# has won the medal but in real that type of situation is not exist oso 
# we have to handle the situation by doing exploratory data analysis)
df[(df['NOC']=='IND')&(df['Medal']== "Gold")]


# In[45]:


medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])


# In[48]:


medal_tally[medal_tally['NOC']=='IND']


# In[59]:


year=df['Year'].unique().tolist()


# In[60]:


year.sort()


# In[61]:


year


# In[ ]:




