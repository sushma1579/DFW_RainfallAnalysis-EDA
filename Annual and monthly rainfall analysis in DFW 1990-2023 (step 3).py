#!/usr/bin/env python
# coding: utf-8

# # Annual and monthly rainfall analysis in DFW 1990-2023

# # STEP 3 : Data Analysis and Visualization 

# # 1. Descriptive Statistics

# In[1]:


# List of all imports
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


path = "E:\Sushma Files\POWER BI TRAINING-Nov 23\Alex the analyst DA Bootcamp\WEB SCRAPING PROJECT\DFW_Rainfall_Analysis_1990_2023_Cleaned.csv"


# In[3]:


df = pd.read_csv(path)


# In[23]:


#df.info()


# In[4]:


df = df.drop(columns = 'Total_Rainfall')

#removing the index column 
df = df.iloc[:,1:14] 

df.info()


# In[5]:


# Monthly descriptive statistics 


# In[6]:


month_data = df.iloc[:,1:13].describe().round(2)
month_data


# # 2. Time Based Analysis 

# # Monthly Patterns  

# In[7]:


#Calculate the average rainfall for each month over all the years.


# In[8]:


monthly_avg_rainfall = df.iloc[:,1:14].mean()
monthly_avg_rainfall = monthly_avg_rainfall.round(2)
monthly_avg_rainfall


# In[ ]:


#Create a line plot or bar plot to visualize the average monthly rainfall.


# In[9]:


plt.figure(figsize=(7,5))
#monthly_avg_rainfall.plot(kind='bar',color='skyblue', edgecolor="black")
plt.bar(monthly_avg_rainfall.index,monthly_avg_rainfall,color='skyblue', edgecolor="black")
plt.title("Monthly average Rainfall 1990-2023")
plt.xlabel("Month")
plt.ylabel("Average Monthly Rainfall")
plt.show()


# In[10]:


#Determine the month with the highest average monthly rainfall (wettest month).


# In[11]:


wettest_month = monthly_avg_rainfall.idxmax()
print("The wettest month is : ",wettest_month)


# In[12]:


#Determine the month with the lowest average monthly rainfall (driest month).


# In[13]:


Driest_month = monthly_avg_rainfall.idxmin()
print("The Driest month is : ",Driest_month)


# # Yearly Patterns 

# In[14]:


# Calculate total_Annual_Rainfall (Sum of the monthly rainfall each year)


# In[15]:


df['Total_Annual_Rainfall'] = df.iloc[:,1:14].sum(axis=1)
df


# In[16]:


# Visualize the Yearly Trends


# In[17]:


plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Total_Annual_Rainfall'], marker='o', linestyle='-')
plt.title('Total Annual Rainfall Over the Years 1990-2023')
plt.xlabel('Year')
plt.ylabel('Total Annual Rainfall (mm)')
plt.grid(True)
plt.show


# In[18]:


# Identify Wettest and Driest Years 


# In[19]:


wettest_year = df.loc[df['Total_Annual_Rainfall'].idxmax()]
print("The wettest year between 1990 and 2023 is/was :",wettest_year['Year'])


# In[20]:


Driest_year = df.loc[df['Total_Annual_Rainfall'].idxmin()]
print("The Driest year between 1990 and 2023 is/was :",Driest_year['Year'])


# # 3. Seasonal Analysis

# In[21]:


# lets create a new data frame with 4 seasons 
#(winter: dec,jan,feb ; spring: mar,apr,may ; summer: jun,jul,aug ; fall: sep,oct,nov)


# In[22]:


df.info()


# In[23]:


# Creating a new data frame with seasons and sum of respected columns data 
Seasonal_Rainfall_Data = pd.DataFrame()
Seasonal_Rainfall_Data['Winter'] = df.iloc[:,[1,2,12]].sum(axis=1)
Seasonal_Rainfall_Data['Spring'] = df.iloc[:,[3,4,5]].sum(axis=1)
Seasonal_Rainfall_Data['Summer'] = df.iloc[:,[6,7,8]].sum(axis=1)
Seasonal_Rainfall_Data['Fall'] = df.iloc[:,[9,10,11]].sum(axis=1)
Seasonal_Rainfall_Data['Year'] = df.iloc[:,[0]]
Seasonal_Rainfall_Data


# In[24]:


#Creating seasonal box plots 
plt.figure(figsize=(12, 6))
Seasonal_Rainfall_Data.boxplot(column=['Winter', 'Spring', 'Summer', 'Fall'], grid=False, showmeans=True)
plt.title('Seasonal Box Plots')
plt.ylabel('Rainfall')
plt.show()


# In[26]:


# visualizing the Average seasonal Rainfall distribution 


# In[27]:


Average_Rainfal_Season = Seasonal_Rainfall_Data.iloc[:,0:4].mean()
Average_Rainfal_Season


# In[28]:


plt.figure(figsize=(7,5))
plt.bar(Average_Rainfal_Season.index,Average_Rainfal_Season,color='skyblue', edgecolor="black")
plt.title('Average Rainfall Across Seasons over 1990-2023')
plt.xlabel('Season')
plt.ylabel('Average Rainfall (mm)')
plt.show()


# # 4. Correlation Analysis

# In[34]:


correlation_matrix = month_data.corr().round(2)
correlation_matrix


# In[ ]:


# Step 3: Visualize with a Heatmap using Matplotlib


# In[35]:


plt.figure(figsize=(10, 8))
heatmap = plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.title('Correlation Matrix - Monthly Data')
plt.colorbar(heatmap, fraction=0.046, pad=0.04)  # Add a colorbar for reference
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.show()

