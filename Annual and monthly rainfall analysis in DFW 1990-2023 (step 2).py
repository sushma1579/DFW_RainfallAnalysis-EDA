#!/usr/bin/env python
# coding: utf-8

# # Annual and monthly rainfall analysis in DFW 1990-2023

# # STEP 2 : Data Cleaning

# In[117]:


import pandas as pd


# In[118]:


path = "E:\Sushma Files\POWER BI TRAINING-Nov 23\Alex the analyst DA Bootcamp\WEB SCRAPING PROJECT\DFW_Rainfall_Analysis_1990_2023.csv"


# In[156]:


df = pd.read_csv(path)
#df


# In[131]:


#df.info()


# In[121]:


df = df.drop(columns = 'Total')


# In[122]:


df = df.replace("T", 0.00)
#df


# In[136]:


numeric_columns = df.columns[1:]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
#df.info()


# In[137]:


#df


# In[149]:


df['Total_Rainfall'] = df.iloc[:,1:13].sum(axis=1)


# In[155]:


#df


# In[152]:


#df.to_csv(r"E:\Sushma Files\POWER BI TRAINING-Nov 23\Alex the analyst DA Bootcamp\WEB SCRAPING PROJECT\DFW_Rainfall_Analysis_1990_2023_Cleaned.csv")

