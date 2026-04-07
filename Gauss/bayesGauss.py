import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "Fruta": ["Manzana","Manzana","Manzana","Naranja","Naranja","Naranja"],
    "Color": ["Rojo","Rojo","Rojo","Naranja","Naranja","Naranja"],
    "Peso": [150, 155, 160, 130, 135, 140],
    "Textura": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

# .map para convertir los colores a valores numéricos | Variables categoricas a numéricas
df['Color'] = df['Color'].map({'Rojo': 0, 'Naranja': 1})
df['Fruta'] = df['Fruta'].map({'Manzana': 0, 'Naranja': 1})

print(df)

# Separar características y etiquetas

X = df[['Color', 'Peso', 'Textura']]

# Variable objetivo

y = df['Fruta']

# Hasta aquí, hemos preparado los datos para el modelo de Naive Bayes. Ahora, vamos a entrenar el modelo y hacer predicciones.

modelo = GaussianNB()
modelo.fit(X, y)

# Hacer predicciones

nuevo = [1,145,1]  # Color: Rojo, Peso: 145, Textura: Lisa
prediccion = modelo.predict([nuevo])
print(f"Predicción para el nuevo dato {nuevo}: {'Manzana' if prediccion[0] == 0 else 'Naranja'}")

# Evaluar el modelo con los datos de entrenamiento (no es lo ideal, pero es un ejemplo)

y_pred = modelo.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Exactitud del modelo: {accuracy:.2f}")
conf_matrix = confusion_matrix(y, y_pred)
print("Matriz de Confusión:")
print(conf_matrix)

# Hacer predicciones
# predicciones = modelo.predict(X)
# print("Predicciones:", predicciones)
# Evaluar el modelo
# accuracy = accuracy_score(y, predicciones)
# conf_matrix = confusion_matrix(y, predicciones)
# print(f"Exactitud: {accuracy:.2f}")
# print("Matriz de Confusión:")  
# print(conf_matrix)

