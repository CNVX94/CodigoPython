from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

data= {
    'correo': [
    "gana dinero rápido",
    "oferta exclusiva gratis",
    "reunión mañana",
    "ajdunto el reporte",
    "gana premio gratis"    
        ],
    'clase':[
        "spam",
        "spam",
        "no_spam",
        "no_spam",
        "spam"
    ]
}

df=pd.DataFrame(data)
print(df)
# Cada fila representa un correo electrónico, y cada numero representa la cantidad de veces que aparece cada palabra en el correo electrónico correspondiente.

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df['correo'])
print(X.toarray())

#Variable objetivo (saber si es spam o no)

y= df['clase']

#Entrenamiento del modelo

modelo = MultinomialNB()
modelo.fit(X,y)

# Matriz vectorizada (X) y la variable objetivo (y) se utilizan para entrenar el modelo de Naive Bayes Multinomial. 
# El modelo aprende a asociar las características de los correos electrónicos con sus respectivas clases (spam o no_spam). 

# Predicción

nuevo_correo = ["reunion mañana"]
nuevo_X = vectorizador.transform(nuevo_correo)
prediccion = modelo.predict(nuevo_X)
print(prediccion)
