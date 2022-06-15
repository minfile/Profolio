# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:00:17 2022

@author: cryst
"""

import pandas as pd

df=pd.read_csv("calendar.csv")
df.shape
df.head()
df.dtypes
df["date"].head()


#convert month and year
df["date"] = pd.to_datetime(df.date)
df["year"] = df.date.dt.year
df["month"] = df.date.dt.month

df_year = df[((df['year'] == 2021) & (df['month'] >= 10))|((df['year'] == 2022)&(df['month'] <= 9))]
df_year= df_year[["listing_id","available","price","year","month"]]
df_year


df_year['available'] = pd.to_numeric(df_year.available)
df_year['busy'] = df_year['available']
df_year.dtypes

temp=pd.pivot_table(df_year,values=['busy'],index=['month'],aggfunc="mean")  
temp.plot.line()

