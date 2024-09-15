# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:19:37 2024

@author: MYBOOK
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <---format of read_csv
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

# summary of the Data
data.info()

var = ['apple', 'banana', 'orange']
var = ('apple', 'banana', 'orange')
var = range (10)
var = {'apple', 'banana', 'orange'}
var = {'Name':'Raj', 'Location':'India'}
var = True

# Working with Calculation
# Defining Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation
# CostPerTransaction = CosrPerItem * NumberofItemPurchased
# Variable = dataframe ['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding a New Column to a DataFrame
# Cost Per Transaction
# data['CostPerTransaction'] = CostPerTransaction
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales Per Transaction
# data['SalesPerTransaction'] = SellingPricePerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased'] 

# Profit Calculation = Sales - Cost 
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales-Cost)/Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
# data['Markup'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']

# Rounding Marking

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# Combining the Data Fields

my_name = 'Raj' + 'Kumar'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

# Checking Column Data Type
print(data['Day'].dtype)

# Changing Columns Data Type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day +'-'+ data['Month']+'-'+ year

data['date'] = my_date

# Using iloc to view the specific columns/rows

data.iloc[0] # Views the row with Index = 0
data.iloc[0:4] # Views the row with Index = 0 to 4
data.iloc[-5:] # Views the last 5 rows

data.head(5) # View the 1st 5 Rows

data.iloc[:,2] # Views 2nd Column of the entire Row
data.iloc[4,2] # Views the 4th Row and its 2nd Column

# Using the split Function to split the Client_keywords field
# new_var = column.str.split('sep' , expand=True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

# Creating a new column for split columns of ClientKeywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# Using replace Function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

# Using the lower function to chqange thr items to Lowercase)

data['ItemDescription'] = data['ItemDescription'].str.lower()

# How to Merge Files
# Bringing in a New Dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# Merging Files: merge_df = pd_merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on='Month')

# Dropping Columns
# df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

# Export in to csv File

data.to_csv('ValueInc_Cleaned.csv', index = False)























