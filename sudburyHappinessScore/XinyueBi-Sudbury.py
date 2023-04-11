#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

df_originA = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'happiness,GDP,le')
df_originB = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'gini')
df_originC = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'safe,pol,pur')
df_originD = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'Regime type')
df_sudbury = pd.read_excel(r'D:\biWork\unCleanData.xlsx', sheet_name = 'sudbury')

df_merged1 = pd.merge(df_originA, df_originB, on = 'Country')

df_merged2 = pd.merge(df_merged1, df_originC, on = 'Country')

df_merged3 = pd.merge(df_merged2, df_originD, on = 'Country')

df_merged3.to_csv('merged_data3.csv', index=False)

list(df_merged3.columns)

# In[ ]:





# In[ ]:




