#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

df_originA = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'happiness,GDP,le')
df_originB = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'gini')
df_originC = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'safe,pol,pur')
df_sudbury = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'sudbury')

df_merged = pd.merge(df_originA, df_originB, on='Country')

df_table = pd.merge(df_merged, df_originC, on = 'Country')

df_table.to_csv('merged_data.csv', index=False)



# In[ ]:





# In[ ]:




