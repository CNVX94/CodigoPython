# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:24:42 2026

@author: isaac
"""

import os #Leer variables del sistema como API Key
import threading #Ejecutar tareas en segundo plano
import tkinter as tk #Interfaz grafica
from tkinter import ttk, messagebox, scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #Convierte texto a numeros
from sklearn.linear_model import LogisticRegression #Modelo de clasificacion
from sklearn.pipeline import Pipeline #Conecta pasos automaticos
from sklearn.model_selection import train_test_split #Divide datos en entrenamiento y prueba
from sklearn.metrics import classification_report,accuracy_score #Medir 
#Gemini SDK oficial actual
from google import genai #Libreria de gemini
#===========================
#CONFIGURACION DE GEMINI
#===========================
API_KEY="AIzaSyAG8AhMBD7NrooyHcPAdXJcrMEd19tjdQA"
def crear_dataset():
    datos=[
        #positivos
        ("La clase estuvo muy clara y entendí todo", "positivo"),
        ("Me gustó mucho la explicación del profesor", "positivo"),
        ("El curso es excelente y muy útil", "positivo"),
        ("Aprendí bastante con los ejercicios", "positivo"),
        ("La actividad fue interesante y divertida", "positivo"),
        ("El contenido está muy bien explicado", "positivo"),
        ("La plataforma funciona muy bien", "positivo"),
        ("Me siento motivado para seguir aprendiendo", "positivo"),
        ("Las prácticas me ayudaron muchísimo", "positivo"),
        ("Todo estuvo muy bien organizado", "positivo"),
        #Negativos
        ("No entendí nada de la clase", "negativo"),
        ("La explicación fue muy confusa", "negativo"),
        ("El sistema falla mucho", "negativo"),
        ("La actividad fue aburrida y complicada", "negativo"),
        ("No me gustó el curso", "negativo"),
        ("Los ejercicios fueron demasiado difíciles", "negativo"),
        ("La plataforma es lenta y se traba", "negativo"),
        ("Estoy frustrado porque no aprendí", "negativo"),
        ("El tema está mal explicado", "negativo"),
        ("No funcionó la práctica", "negativo"),
        #Neutrales
        ("La clase fue hoy en la mañana", "neutral"),
        ("Entregué la tarea en la plataforma", "neutral"),
        ("El examen será el viernes", "neutral"),
        ("Revisé el material del curso", "neutral"),
        ("El profesor dejó una actividad", "neutral"),
        ("Hoy tuvimos laboratorio", "neutral"),
        ("Subí mi archivo al sistema", "neutral"),
        ("La sesión duró dos horas", "neutral"),
        ("Hay una tarea pendiente", "neutral"),
        ("Leí las instrucciones del ejercicio", "neutral"),
        ]
    df=pd.DataFrame(datos,columns=["texto","etiqueta"])
    return df
class ClasificadorComentarios:
    def __init__(self):
        self.modelo=Pipeline([
            ("tfidf",TfidfVectorizer(lowercase=True,stop_words=None)),
            ("clf",LogisticRegression(max_iter=1000))
            ])
        self.esta_entrenado=False
        self.reporte=""
        self.accuracy=None
    def entrenar(self,df):
        X=df["texto"]
        y=df["etiqueta"]
        X_train,X_test,y_train,y_test=train_test_split(
            X,y,test_size=0.25,
            random_state=42,
            stratify=y)
        self.modelo_fit(X_train,y_train)
        y_pred=self.modelo.predict(X_test)
        self.accuracy=accuracy_score(y_test, y_pred)
        self.reporte=classification_report(y_test, y_pred,digits=4)
        self.esta_entrenado=True
        return self.accuracy,self.reporte
    def predecir(self,texto):
        if not self.esta_entrenado:
            raise ValueError("El modelo aún no ha sido entrenado.")
        pred=self.modelo.predict([texto])[0]
        probs=self.modelo.predict_proba([texto])[0]
        clases=self.modelo.classes_
        resultados={clase:float(prob) for clase,prob in zip(clases,probs)}
        confianza=max(resultados.values())
        return pred,resultados,confianza
#========================================
#FUNCION PARA EXPLICACION CON GEMINI
#========================================
def explicacion_con_gemini(texto,prediccion,probabilidades):
    if not API_KEY:
        return(
            "No se encontró la API key de Gemini.\n\n"
            "Coloca tu clave en la variable API_KEY o en la variable de entorno GEMINI_API_KEY"
            )
    try:
        client=genai.client(api_key=API_KEY)
        prompt=f"""
        Eres un asistente experto en análisis educativo.
        Tengo un modelo de machine learning que clasificó el siguiente comentario:
        Texto: "{texto}"
        Predicción del modelo: {prediccion}
        Probabilidades aproximadas:
        {probabilidades}
        Tu tarea:
        1. Explica por qué ese comentario puede pertenecer a esa categoría.
        2. Haz una explicación breve, clara y en español.
        3. Sugiere una acción pedagógica si el comentario es negativo.
        4. No inventes datos técnicos no proporcionados.
        """
        response=client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
            )
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        return "Gemini no devolvió texto."
    except Exception as e:
        return f"Error al conectar con Gemini:\n{str(e)}"