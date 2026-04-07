import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Sentiment Labelled Sentences Data Set | Multinomial Naive Bayes para clasificación de texto

df = pd.read_csv("amazon_cells_labelled.txt", delimiter="\t", header=None, names=["Review", "Sentiment"])

print(df.head())

# Contamos el número de palabras de cada texto.

print(df['Sentiment'].value_counts())

# Crear el modelo de Native Bayas Multinomial

vectorizar = CountVectorizer()
X = vectorizar.fit_transform(df['Review'])
y = df['Sentiment']

# Entrenamos el modelo

modelo = MultinomialNB()
modelo.fit(X,y)

# Predicción

ejemplos = ['This weekend i like to smoke some weed', 'My primo is feeling sad', 'hi brother, im feeling so sick']
ejemplos_vector = vectorizar.transform(ejemplos)
prediccion = modelo.predict(ejemplos_vector)
print(prediccion)

# Evaluar modelo

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3) # División de datos

modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precision: {accuracy:.2f}")

#=== Notas IA ===#

# Convertir las reseñas a una matriz de características utilizando CountVectorizer

# vectorizer = CountVectorizer()

# X = vectorizer.fit_transform(df['Review'])
# y = df['Sentiment']

# # Dividir los datos en conjuntos de entrenamiento y prueba

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Entrenar el modelo de Naive Bayes Multinomial

# modelo = MultinomialNB()
# modelo.fit(X_train, y_train)

# # 

# # Hacer predicciones

# y_pred = modelo.predict(X_test)

# # Evaluar el modelo

# accuracy = accuracy_score(y_test, y_pred)

# print(f"Exactitud del modelo: {accuracy:.2f}")

# conf_matrix = confusion_matrix(y_test, y_pred)

# print("Matriz de Confusión:")

# print(conf_matrix)

