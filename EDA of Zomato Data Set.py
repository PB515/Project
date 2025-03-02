#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import os


# In[5]:


os.chdir("E:\\Project\\Python\\AI ML Project\\EDA & Feature Engineering\\Zomatodataset")


# In[10]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[11]:


df.columns


# In[12]:


df.info()


# In[15]:


df.describe()


# In[16]:


df.isnull().sum()


# In[18]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[21]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[59]:


df_country=pd.read_excel('new.xlsx')


# In[60]:


df_country.head()


# In[61]:


df_final=pd.merge(df,df_country, on='Country Code' , how="left")


# In[53]:


df.columns


# In[62]:


df_final.head(2)


# Observation on zomato's country code

# In[64]:


Country_name=df_final.Country.value_counts().index


# In[65]:


Country_value=df_final.Country.value_counts().values


# Ploting pie chart of top 3 countries zomato is present

# In[71]:


plt.pie(Country_value[:3],labels=Country_name[:3],autopct='%1.2f%%')


# In[72]:


df.columns


# In[76]:


Ratings=df_final.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[ ]:


##conclusion and Observation 


# In[77]:


Ratings.head()


# In[82]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating',y='Rating Count',data=Ratings)


# In[84]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating',y='Rating Count',hue='Rating color',palette=['white','red','orange','yellow','green','green'],data=Ratings)


# Observation
# 1)Not rated are very high
# 2)Max ratings are from 2.5to 4.5

# In[85]:


## Count Plot
sns.countplot(x='Rating color',data=Ratings,palette=['white','red','orange','yellow','green','green'])


# Gives how Frequent rating color is
# here orange has most no of rating frequency that means it has more rating values than any other.

# In[86]:


Ratings


# In[87]:


df_final.columns


# In[90]:


zeror=df_final.groupby(['Rating color','Country']).size().reset_index().rename(columns={0:'Rating Count'})


# In[91]:


zeror


# In[93]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Rating color',y='Rating Count',data=Ratings)


# In[106]:


df_final[df_final['Rating color']=='White'].groupby('Country').size().reset_index()


# In[107]:


df_final.columns


# In[115]:


df_final[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[116]:


df_final.columns


# In[118]:


df_final[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index()


# In[127]:


top10=df_final[['Cuisines','Rating color']].groupby(['Cuisines','Rating color']).size().reset_index()


# In[133]:


top10


# In[132]:


top10[top10['Rating color']=='Dark Green'].groupby('Rating color').size().reset_index()

