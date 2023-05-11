#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:28:36 2023

@author: jomaicalei

Let's encode a few variables first before we engineer our ML models.

Variables to be encoded: 6
- department (Men, Women, Unisex?, Kids Unisex?)
- concentration ( EDT, EDP, PDT, Oil, EDC)
- scents
- base_note
- middle_note
- item_rating
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/Users/jomaicaalfiler/Desktop/ScentAI/models/raw_noon.csv')

# We encode each of the variables: 
# we need to create dummy variables first, 
# then drop orignal column.
df_dummies = pd.get_dummies(df['department'], prefix='department')
df = pd.concat([df, df_dummies], axis=1)
df.drop('department', axis=1, inplace=True)

df_dummies = pd.get_dummies(df['concentration'], prefix='concentration')
df = pd.concat([df, df_dummies], axis=1)
df.drop('concentration', axis=1, inplace=True)

df_dummies = pd.get_dummies(df['scents'], prefix='scents')
df = pd.concat([df, df_dummies], axis=1)
df.drop('scents', axis=1, inplace=True)

df_dummies = pd.get_dummies(df['base_note'], prefix='base_note')
df = pd.concat([df, df_dummies], axis=1)
df.drop('base_note', axis=1, inplace=True)

df_dummies = pd.get_dummies(df['middle_note'], prefix='middle_note')
df = pd.concat([df, df_dummies], axis=1)
df.drop('middle_note', axis=1, inplace=True)

df_dummies = pd.get_dummies(df['item_rating'], prefix='item_rating')
df = pd.concat([df, df_dummies], axis=1)
df.drop('item_rating', axis=1, inplace=True)


# view all column names before saving it to a csv file
print(df.columns)

# save the encoded DataFrame to a CSV file
df.to_csv('encoded_data.csv', index=False)


# Everything is encoded !!! 0 = absent, 1 = present



# counting the discrete variables for each of the columns (ALL columns)
# print(df['department'].value_counts()) -----> (Men, Women, Unisex, Kids Unisex)

# print specific column to double check (if it was dropped)
# print(df['concentration']) ----> KeyError means it is dropped


# ------------------------------------------------

# # Another way to encode it using sklearn
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# df_model = pd.read_csv('path/to/your/csv/file.csv')

# # create a LabelEncoder object
# le = LabelEncoder()

# df_model['department'] = le.fit_transform(df_model['department'])
# df_model['concentration'] = le.fit_transform(df_model['concentration'])
# df_model['scents'] = le.fit_transform(df_model['scents'])
# df_model['base_note'] = le.fit_transform(df_model['base_note'])
# df_model['middle_note'] = le.fit_transform(df_model['middle_note'])
# df_model['item_rating'] = le.fit_transform(df_model['item_rating'])

# # save the encoded DataFrame to a CSV file
# df_model.to_csv('encoded_data.csv', index=False)






