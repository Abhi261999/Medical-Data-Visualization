# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:07:46 2024

@author: Acer
"""
#git
#Bussiness constraints= Improve customer experience by analysing sales data
#Bussiness constraints = Increase revenue

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\medical_my.csv")
df.shape

df.head(10)

import datetime as dt

df['Dateofbill'] = df['Dateofbill'].dt.strftime(text_data,'%d-%m-%Y')
print()
#objective = imporve customer experience by analysing sales data
#increase revenue

df.info()

df.drop(['Patient_ID'], axis = 1,inplace =True)

pd.isnull(df)

pd.isnull(df).sum()

df.shape

#dropping the null values
df.dropna(inplace =True)

df.columns

#lets rename
df.rename(columns={'DrugName':'DawaA'} ,inplace = True)
df.columns
df.describe()

#use describe for specific columns

df[['Final_Cost','Final_Sales']].describe()

#EXPLORATERORY DATA ANALYSIS

ax = sns.countplot( x = 'Typeofsales' ,data = df)
for bars in ax.containers:
    ax.bar_label(bars)
    
df.groupby(['Typeofsales'],as_index = False)['Final_Cost'].sum().sort_values(by='Final_Cost',ascending = False)

sales_new = df.groupby(['Typeofsales'],as_index = False)['Final_Cost'].sum().sort_values(by='Final_Cost',ascending = False)

sns.barplot(x = 'Typeofsales' , y = 'Final_Cost' , data = sales_new)

#from the above graph we can say that return is frequent as compared to sales

df.groupby(['Dept'],as_index = False)['Final_Sales'].sum().sort_values(by = 'Final_Sales',ascending = False)

sales_dept = df.groupby(['Dept'],as_index = False)['Final_Sales'].sum().sort_values(by = 'Final_Sales',ascending = False)

sns.barplot(x = 'Dept' , y = 'Final_Sales' ,data = sales_dept)

#from the above graph we can say that department1 is on hipe with respect to sales

df.groupby(['Dept'],as_index = False)['ReturnQuantity'].sum().sort_values(by = 'ReturnQuantity',ascending = False)

dept_ret =df.groupby(['Dept'],as_index = False)['ReturnQuantity'].sum().sort_values(by = 'ReturnQuantity',ascending = False)

sns.barplot(x = 'Dept', y = 'ReturnQuantity', data =dept_ret )

#all of the return items are from the department 1 only so we can retain with customers that the product brought 
#from department will not have the return policy.

df.groupby(['Specialisation'],as_index = False)['Quantity'].sum().sort_values(by = 'Quantity',ascending = False)

spe_quanti = df.groupby(['Specialisation'],as_index = False)['Quantity'].sum().sort_values(by = 'Quantity',ascending = False).head(5)
sns.set(rc={"figure.figsize":(15,5)})
sns.barplot(x = 'Specialisation' ,y = 'Quantity' , data= spe_quanti)

#from this graph we are clear about max quantity of order quantity of specialisation4 , specialization7 and specialisation8 is sold out .















    
    

