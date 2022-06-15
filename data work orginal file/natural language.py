# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:23:39 2022

@author: cryst
"""


#natural language
import pandas as pd
df=pd.read_csv("reviews.csv")


df["date"] = pd.to_datetime(df.date)	
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year
#since the database dones't have 2022 data, so i use 2021 instand
df_year = df[((df['year'] == 2021))|((df['year'] == 2022)&(df['month'] <= 9))]

df_year.dtypes

# 3.1 store comments data into one variable
feature = []
for i in range(0,len(df_year.index)):
    feature.append(df_year.iloc[i,5])
feature


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
  
  
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(str(feature))

filtered_sentence = []
for word in word_tokens: 
    if word not in stop_words:
        filtered_sentence.append(word)
  
import nltk        
tkq=nltk.FreqDist(filtered_sentence)

df = pd.DataFrame()
df['Keyword'] 
df['Frequency']

keyword = []
frequency = []
for i,j in tkq.most_common(50):
        if len(i)>2:
            print(i,j)
            keyword.append(i)
            frequency.append(j)
df['Keyword'] = keyword
df['Frequency'] = frequency            
df            
df.plot.bar(x="Keyword",y="Frequency")
