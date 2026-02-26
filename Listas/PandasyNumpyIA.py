#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:28:46 2026

@author: cnvx94
"""

#Pandas

# Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Crear serie a partir de una lista
s=pd.Series(['Matemáticas',
             'Historia',
             'Economia',
             'Programación',
             'Inglés'],dtype='string')

print(s)
#Operaciones mátematicas
serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([9,8,7,6,5])
serie3 = serie1+serie2

print(serie3) # o print(serie1+serie2)


#Operaciones relaciónales
opr = serie1<serie2
print(opr)

#Series iguales
opr = serie1 == serie2
print(opr)

#Series a partir de un diccionario
s2=pd.Series({
    'matematicas':6,
    'economia':8,
    'programacion':8
    })

print(s2)

#Propiedades

#s2.size()
#s2.index()
#s2.dtype()
print(s2[2])

#Acceder a los datos
s2[2]
s2['programacion']
s2[['economia', 'programacion']]
s2.count()
s2.sum()
s2.cumsum() #Suma acumulada de todos los datos númericos
s2.max()
s2.min()
s2.var() #Varianza
s2.std() #Desviación estandar
s2.describe() #Datos estádisticos

# Data Frames
# Objeto que se define como un conjunto de datos estructurado.
# Sql, csv, diccionarios, etc
# Practica utilizando un diccionario

datos=({
        'nombre':['Maria','Luis','Carmen','Antonio'],
        'edad':[18,22,20,21],
        'materia':['matematicas', 'AC', 'IA','SO'],
        'correos':['mar@correo.com','luis@correo.com','carmen@correo.com','antonio@correo.com']
        })

df=pd.DataFrame(datos)

print(df)
#Crear dataframe a partir de una lista de listas

df1=pd.DataFrame([['Maria',18],
                  ['Luis',20],
                  ['Carmen',20]],
                  columns=['Nombre','Edad'])

# Dataframe a partir de una lista de diccionarios

df2=pd.DataFrame(([{'Nombre':'Maria','Edad':18},
                   {'Nombre':'Carmen','Edad':22},
                   {'Nombre':'Carmen','Edad':20},]))

## Crear dataframe a partir de un arrar de numpy

df3=pd.DataFrame(np.random.randn(4,3),
                 columns=['a','b','c'])

#Analizar propiedades de los dataframes

df2.info()
df2.shape
df2.size #N elementos
df2.index#Index, dondé empieza y donde termina
df2.head(10)#Primeros n materiales
df2.tail(3)#Ultimos n materiales                  

##  Actividad 
    
print("--Actividad--")
#Serie que tenga como datos los números 1,2,3,4
#Como índices Eu, Alemania, Colombia, Japón

serieNum = pd.Series({
    1:'EU',
    2:'Alemania',
    3:'Colombia',
    4:'Japon'
    })
print(serieNum[4])

#Ejercicio dos, añadir un jugador

serieJug = pd.Series({
    1:'Juan',
    2:'Matias',
    3:'Gonzalo'
    })

serieJug.loc[10]='Cesar'
print(serieJug)

# Dataframe Contabilidad

dfConta = pd.DataFrame({
    'meses':['Enero','Febrero','Marzo','Abril'],
    'ventas':[30500,35600,28300,33900],
    'gastos':[22000,23400,18100,20700]
    })

print(dfConta)

x = np.arange(len(dfConta))  # positions for each month (0,1,2,3)
width = 0.35                 # width of the bars

fig, ax = plt.subplots(figsize=(8, 5))

# Plot bars
bars1 = ax.bar(x - width/2, dfConta['ventas'], width, label='Ventas', color='steelblue')
bars2 = ax.bar(x + width/2, dfConta['gastos'], width, label='Gastos', color='darkorange')

# Customize axis
ax.set_xlabel('Meses')
ax.set_ylabel('Monto')
ax.set_title('Ventas vs Gastos por Mes')
ax.set_xticks(x)
ax.set_xticklabels(dfConta['meses'])
ax.legend()

# Optional: Add value labels on top of bars
ax.bar_label(bars1, fmt='%.0f', padding=3)
ax.bar_label(bars2, fmt='%.0f', padding=3)

plt.tight_layout()
plt.show()