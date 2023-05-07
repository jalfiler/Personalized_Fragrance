#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:28:36 2023

@author: jomaicalei

We will be using this cleaned dataset for our building our models
"""

import pandas as pd

df = pd.read_csv('raw_noon.csv') # raw data

# use one-hot encoding to convert department into a numerical variable (0 = false, 1 = true)
df_2 = pd.concat([df, pd.get_dummies(df['department'], prefix='department')], axis=1)

# Perform one-hot encoding on the concentration column (0 = false, 1 = true)
df_2 = pd.concat([df_2, pd.get_dummies(df_2['concentration'], prefix='concentration')], axis=1)

# save tidy data into a csv file
df_2.to_csv('tidy_noon.csv', index=False)
