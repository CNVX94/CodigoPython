from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Creando el dataframe para poder determinar si un mensaje es bueno o malo.

data= {
    'Reseña': [
    "funciona excelente",
    "Muy buena calidad",
    "el producto llego dañado",
    "muy mala calidad",
    "Excelente producto y calidad"
    ],
    'Clase': [
        "bueno",
        "bueno",
        "malo",
        "malo",
        "bueno"
    ]
}

df=pd.DataFrame(data)
print(df)

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df['Reseña'])
print(X.toarray())

y = df['Clase']
modelo = MultinomialNB()
modelo.fit(X, y)

nuevo_correo = ["producto de mala calidad"]
nuevo_X = vectorizador.transform(nuevo_correo)
prediccion = modelo.predict(nuevo_X)
print(prediccion)