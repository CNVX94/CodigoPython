# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:21:39 2026

@author: desarrollo 6
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

#Datos
df=pd.read_csv("WineQT.csv")

print(df)

print(df.shape)
print(df.describe())

df=df.iloc[:,:-1]

print(df)

print(df.describe())
print(df.info())

# Visualizar la relacion de las variables
plt.figure(figsize=(8,6))
sns.scatterplot(x='fixed acidity', y='volatile acidity', data=df, color='blue')
plt.title('Relación entre acidez fija y acidez volátil')
plt.xlabel('Acidez fija')
plt.ylabel('Acidez volátil')
plt.show()

# Scatter plot para acido citrico y azucar residual
plt.figure(figsize=(8,6))
sns.scatterplot(x='citric acid', y='residual sugar', data=df, color='green')
plt.title('Relación entre ácido cítrico y azúcar residual')
plt.xlabel('Ácido cítrico')
plt.ylabel('Azúcar residual')
plt.show()

## Scatter plot para fixed total sulfur dioxide vs density
plt.figure(figsize=(8,6))
sns.scatterplot(x='total sulfur dioxide', y='density', data=df, color='red')
plt.title('Relación entre dióxido de azufre total y densidad')
plt.xlabel('Dióxido de azufre total')
plt.ylabel('Densidad')
plt.show()
