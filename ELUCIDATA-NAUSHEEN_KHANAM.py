#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import seaborn as sns
from pandas import read_csv
# load dataset
df= pd.read_csv("data.csv")
df.head()


# In[60]:


df.info()


# In[61]:


print(df.isnull().sum()) #missing values


# In[33]:


#imputation of missing values
d=pd.read_csv("data.csv")
updated_df1= d
updated_df1['radius_mean']=updated_df1['radius_mean'].fillna(updated_df1['radius_mean'].mean())
updated_df1['area_mean']=updated_df1['area_mean'].fillna(updated_df1['area_mean'].mean())
updated_df1.head()


# In[62]:


#What does the distribution of each of those features look like? Explain your answer with the help of graphs and summary statistics

import pandas as pd
import matplotlib.pyplot as plt

df = [[842302, 'M' ,17.99, 10.38, 122.80, 1001.0, 0.11840, 0.27760, 0.3001, 0.14710, 25.38, 17.33, 184.60, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.11890]]
df = pd.DataFrame(data, columns = ['id', 'diagnosis', 'radius_mean','texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean','compactness_mean', 'concavity_mean','concave_points_mean', 'radius_worst', 'texture_worst', 'perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst','concave_points_worst','symmetry_worst','fractal_dimension_worst'])
df.hist()
  
# show plot
plt.show()


# In[48]:


#preprocossing
#dropping the id column and removing the columns having NaN values
df = df.drop(['id'], axis=1)
#encoding the the target feature
df['diagnosis']= df['diagnosis'].replace('M', 1)
df['diagnosis']= df['diagnosis'].replace('B', 0)
#plotting the corellation matrix
corr = df.corr()
plt.figure(figsize=(18,18))
sns.heatmap(corr, cmap='coolwarm', annot = True)
plt.show()
#Correlation matrix
cc=corr[abs(corr['diagnosis']) > 0.5].index
acc=df[df.columns[:]].corr()['diagnosis']
print('All features  with thier correlations is: \n',acc)


# In[ ]:





# In[51]:


#QUESTION 5

#finding out the positively corelated feature
cc=corr[abs(corr['diagnosis']) > 0.5].index
print('- Number of most correlated features = ', len(cc))
print('--------------------------------------------------')
print('- Most correlated features is: \n ',cc)
acc=df[df.columns[:]].corr()['diagnosis']
print('All features  with thier correlations is: \n',acc)


# In[52]:


#finding out the negatively corelated feature
cc2=corr[abs(corr['diagnosis']) <= 0.5].index
print('- Number of Least correlated features = ', len(cc2))
print('--------------------------------------------------')
print('- Least correlated features is: \n ',cc2)


# In[57]:


#selecting most essential features
df = df[['diagnosis', 'radius_mean', 'area_mean',
       'compactness_mean', 'concavity_mean', 
       'perimeter_worst', 'area_worst', 'compactness_worst',
       'concavity_worst','texture_mean', 
         'smoothness_mean', 
         'texture_worst', 'smoothness_worst', 'symmetry_worst',
       'fractal_dimension_worst']]
df.head()
print(df.shape)
df.tail(10)


# In[63]:


fig, ax = plt.subplots(ncols=5, nrows=4, figsize=(30,20))
index = 0
ax = ax.flatten()
for col, value in df.items():
    col_dist = sns.histplot(value, ax=ax[index], color="blue", label="100% Equities", kde=True, stat="density", linewidth=0)
    col_dist.set_xlabel(col,fontsize=18)
    col_dist.set_ylabel('density',fontsize=18)
    index += 1
plt.tight_layout(pad=0.5, w_pad=0.7, h_pad=5.0)


# In[ ]:




