# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:34:39 2024

@author: mayte
"""

import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Función para predecir si el usuario tiene cáncer de mama
def predecir_cancer():
    # Obtener los valores ingresados por el usuario
    Clump_Thickness= float(txt1.get())
    Uniformity_of_Cell_Size = float(txt2.get())
    Uniformity_of_Cell_Shape = float(txt3.get())
    Marginal_Adhesion = float(txt4.get())
    Single_Epithelial_Cell_Size = float(txt5.get())
    Bare_Nuclei=float(txt6.get())
    Bland_Chromatin=float(txt7.get())
    Normal_Nucleoli=float(txt8.get())
    Mitoses=float(txt9.get())
    
    # Crear un arreglo con los valores ingresados
    new_data = [[Clump_Thickness, Uniformity_of_Cell_Size, Uniformity_of_Cell_Shape, Marginal_Adhesion, 
                 Single_Epithelial_Cell_Size, Bare_Nuclei, Bland_Chromatin, Normal_Nucleoli, Mitoses]]
    
    
    
    # Realizar la predicción utilizando el modelo
    prediction = logreg.predict(new_data)
    prediction
    
    # Mostrar el resultado al usuario
    if prediction[0] == 0:
        messagebox.showinfo("Resultado", "No tiene cáncer de mama.")
    else:
        messagebox.showinfo("Resultado", "Tiene cáncer de mama.")

# Cargar el conjunto de datos de cáncer de mama de Wisconsin
#cancer = load_breast_cancer()
df=pd.read_csv("breast_cancer.csv")
#contar los valores de las clases
df['Class'].value_counts()

df['Class'].replace(2,0,inplace=True)
df['Class'].replace(4,1,inplace=True)
X = df.drop(['Class'], axis=1)
y = df['Class']


# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

x_train.shape , x_test.shape

cols=x_train.columns

#estandarizar las caracteristicas de un conjunto de datos, para que tengan una media de cero 
#y desviaci[on estandar de 1, lo cual significa que los datos estaran centrados alrededor de 0.
#lo cual pude ser util para al;goritmos que asumen que las caracteristicas tienen una distribucion normal
# y que funcionan mejor cuando las caracteristicas estan en la misma escala.

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

#transformarlos a dataframe de nuevo

x_train = pd.DataFrame(x_train, columns=cols)
x_test = pd.DataFrame(x_test, columns=cols)


# Entrenar el modelo de regresión logística
#crear el modelo e regresion logistica
logreg=LogisticRegression(random_state=0)
#entrenar el modelo
logreg.fit(x_train, y_train)

#=============================diseño de ventana de innterfaz===================
# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Predicción de Cáncer de Mama")
#dimensiones de la ventana
root.geometry('650x500')
#color de foondo
root.config(bg='#25E6C9')

#=============Etiquetas de entradas de datos============
#Etiqueta de entrada 1
lbl1=tk.Label(root, text="Espesor: ", bg='#25E6C9')
lbl1.place(x=100, y=10, width=150, height=30)

#caja de texto1
txt1=tk.Entry(root)
txt1.place(x=280, y=10, width=150, height=30)

#Etiqueta de entrada 2
lbl2=tk.Label(root, text="tamanio de la celula: ", bg='#25E6C9')
lbl2.place(x=100, y=50, width=180, height=30)

#caja de texto2
txt2=tk.Entry(root)
txt2.place(x=280, y=50, width=150, height=30)

#Etiqueta de entrada 3
lbl3=tk.Label(root, text="forma celular: ", bg='#25E6C9')
lbl3.place(x=100, y=90, width=180, height=30)

#caja de texto3
txt3=tk.Entry(root)
txt3.place(x=280, y=90, width=150, height=30)

#Etiqueta de entrada 4
lbl4=tk.Label(root, text="Adesion marginal: ", bg='#25E6C9')
lbl4.place(x=100, y=130, width=180, height=30)

#caja de texto4
txt4=tk.Entry(root)
txt4.place(x=280, y=130, width=150, height=30)

#Etiqueta de entrada 5
lbl5=tk.Label(root, text="Tam. cel epitelial: ", bg='#25E6C9')
lbl5.place(x=100, y=170, width=180, height=30)

#caja de texto5
txt5=tk.Entry(root)
txt5.place(x=280, y=170, width=150, height=30)

#Etiqueta de entrada 6
lbl6=tk.Label(root, text="Nucleos desnudos: ", bg='#25E6C9')
lbl6.place(x=100, y=210, width=180, height=30)

#caja de texto 6
txt6=tk.Entry(root)
txt6.place(x=280, y=210, width=150, height=30)

#Etiqueta de entrada 7
lbl7=tk.Label(root, text="cromatina suave: ", bg='#25E6C9')
lbl7.place(x=100, y=250, width=180, height=30)

#caja de texto 7
txt7=tk.Entry(root)
txt7.place(x=280, y=250, width=150, height=30)

#Etiqueta de entrada 8
lbl8=tk.Label(root, text="Nucleolos normales: ", bg='#25E6C9')
lbl8.place(x=100, y=290, width=180, height=30)

#caja de texto 7
txt8=tk.Entry(root)
txt8.place(x=280, y=290, width=150, height=30)


#Etiqueta de entrada 6
lbl9=tk.Label(root, text="Mitosis: ", bg='#25E6C9')
lbl9.place(x=100, y=330, width=180, height=30)

#caja de texto 6
txt9=tk.Entry(root)
txt9.place(x=280, y=330, width=150, height=30)

# Botón para realizar la predicción
button = tk.Button(root, text="Predecir", command=predecir_cancer)
button.place(x=150, y=400, width=150, height=30)


# Ejecutar el bucle principal de la aplicación
root.mainloop()
