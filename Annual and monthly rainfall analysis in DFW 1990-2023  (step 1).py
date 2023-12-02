#!/usr/bin/env python
# coding: utf-8

# # Annual and monthly rainfall analysis in DFW 1990-2023

# # STEP 1 : Web Scraping 

# In[212]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[213]:


url = 'https://www.weather.gov/fwd/dmoprecip'


# In[230]:


page = requests.get(url) # response model type
#print(type(page))
#print(page)


# In[232]:


Soup = BeautifulSoup(page.text, 'html') # BeautifulSoup instance/ object
#print(type(Soup))
#print(Soup)


# In[216]:


table = Soup.find_all('table', class_='nrml') # result set 
#print(type(table))
table = table[0]
table = table.find_all('tr')
#print(table)


# In[227]:


table_titles = [i.text.strip() for i in table]
#print(type(table_titles))
#print(table_titles[0])

table_titles[1] += '\nT\nT\nT' # since there are values missing for 2 months and Total in 2023 
#print(table_titles[1])

table_column_names = []

for i in table_titles[0:1]:
    table_column_names.append(i.split('\n'))

#print(table_column_names)


# In[218]:


df = pd.DataFrame(columns = table_column_names )
df


# In[220]:


row_data = []
for i in table_titles[1:35]:
        row_data.append(i.split('\n'))

for i in range(0,len(row_data)):
    df.loc[i] = row_data[i]
df


# In[ ]:


# Now exporting the data to a csv file in a target location 


# In[228]:


df.to_csv(r'E:\Sushma Files\POWER BI TRAINING-Nov 23\Alex the analyst DA Bootcamp\WEB SCRAPING PROJECT\DFW_Rainfall_Analysis_1990_2023.csv',index = False)

