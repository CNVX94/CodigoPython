# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:29:30 2024

@author: mayte
"""

#==============Ejercicio de regresion lineal para vinos==========
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.metrics import mean_squared_error

#datos
df=pd.read_csv("WineQT.csv")


#dar el tamanio del df
df.shape

#dar la descripcion estadistica
df.describe()

#eliminar las ultima columna
df=df.iloc[:,:-1]
#mostrar los resultados
print(df)
#hacer nuevamente la descripcion estadistica
df.describe()
#dar la informacion de las varibales
df.info()

#===============visualizar la relacion de las variables=============================
#visualizar la informacion de la variable fixed acidity vs volatile acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='fixed acidity', y='volatile acidity', data=df, color='blue')
plt.title('Scatter Plot of Fixed Acidity vs Volatile Acidity')
plt.xlabel('Fixed Acidity')
plt.ylabel('Volatile Acidity')
plt.show()

# Scatter plot for citric acid vs residual sugar
plt.figure(figsize=(8, 6))
sns.scatterplot(x='citric acid', y='residual sugar', data=df, color='green')
plt.title('Scatter Plot of citric acid and residual sugar')
plt.xlabel('citric acid')
plt.ylabel('residual sugar')
plt.show()

# Scatter plot for fixed acidity vs volatile acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='chlorides', y='free sulfur dioxide', data=df, color='red')
plt.title('Scatter Plot of chloride and free sulphure dioxide')
plt.xlabel('chlorides')
plt.ylabel('free sulfur dioxide')
plt.show()

# Scatter plot for fixed total sulfur dioxide vs density
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total sulfur dioxide', y='density', data=df, color='purple')
plt.title('Scatter Plot of total surface dioxide and  density ')
plt.xlabel('total sulfur dioxide ')
plt.ylabel('density')
plt.show()

# Scatter plot for fixed acidity vs volatile acidity
plt.figure(figsize=(8, 6))
sns.scatterplot(x='pH', y='sulphates', data=df, color='orange')
plt.title('Scatter Plot of pH and sulphate')
plt.xlabel('pH ')
plt.ylabel('sulphates')
plt.show()

#haz un heatmap para ver la correlacion entre variables
correlation_matrix = df.corr()

#plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
sns.heatmap(correlation_matrix)
plt.title('Correlation Matrix')
plt.show()

#=============================crear el modelo de regresion =========================
X=df.drop('quality', axis=1)
y=df.quality

#separar los datos en entrenamieto y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

#seleccionar modelo
modelo=LinearRegression()

#Entrenar el modelo
modelo.fit(X_train, y_train)

#coeficiente de determinacion
modelo.score(X_test, y_test)


#coeficientes
coef=modelo.coef_
coef
#intercepto
intercep=modelo.intercept_
intercep

print("Ecuacion de la recta: y =",(coef),"xi+",intercep)

#Realizar predicciones
predicciones=modelo.predict(X_test)
print(predicciones[0:3,])

#revisar el error
rmse=root_mean_squared_error(
    y_true=y_test,
    y_pred=predicciones,
    squared=False)
rmse