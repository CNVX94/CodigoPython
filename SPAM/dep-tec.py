from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

data = {
    "Titular":[
        "equipo gana campeonato",
        "nuevo telefono inteligente",
        "jugador gana gol decisivo",
        "empresa lanza nueva computadora",
        "equipo gana torneo"
    ],
    "Categoria":[
        "deportes",
        "tecnologia",
        "deportes",
        "tecnologia",
        "deportes"
    ]
}

df = pd.DataFrame(data)
print(df)
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df['Titular'])
print(X.toarray())
y = df['Categoria']
modelo = MultinomialNB()
modelo.fit(X, y)

nuevo_titular = ["nuevo equipo gana"]
print("Nuevo titular:", nuevo_titular)
nuevo_X = vectorizador.transform(nuevo_titular)
prediccion = modelo.predict(nuevo_X)
print(prediccion)