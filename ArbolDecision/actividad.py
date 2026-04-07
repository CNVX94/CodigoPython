
import pandas as pd
import matplotlib.pyplot as plt
# Modelo de datos de decisión.
from sklearn import tree
#Convierte el texto a números
from sklearn.preprocessing import LabelEncoder
#Entrenamiento y prueba
from sklearn.model_selection import train_test_split
#modelo de arbol de decisión
from sklearn.tree import DecisionTreeClassifier
#graficar el arbol 
from sklearn.tree import plot_tree
#matrices de evaluacion
from sklearn.metrics import accuracy_score, confusion_matrix
#import pydotplus

#Leer los datos
dataset=pd.read_csv("Pacientes2.csv")
dataset.shape

#Leer las primeras 5 filas
dataset.head()

#Nombre de las columnas
dataset.columns

#Renombrar las olumnas para facilitar la lectura
# dataset.columns=['Age','Gender','Polyuria','Polydipsia','Sudden','Weakness','Polyphagia','Genital',
# 'Visual','Itching','Irritability','Delayed','Partial','Muscle', 'Alopecia', 'Obesity','Clase' ]

dataset.columns

#Transformar las variables categoricas a numericas

le=LabelEncoder()

dataset.Gender=le.fit_transform(dataset.Gender)
dataset.Polyuria=le.fit_transform(dataset.Polyuria)
dataset.Polydipsia=le.fit_transform(dataset.Polydipsia)
dataset.Sudden=le.fit_transform(dataset.Sudden)
dataset.Weakness=le.fit_transform(dataset.Weakness)
dataset.Polyphagia=le.fit_transform(dataset.Polyphagia)
dataset.Genital=le.fit_transform(dataset.Genital)
dataset.Visual=le.fit_transform(dataset.Visual)
dataset.Itching=le.fit_transform(dataset.Itching)
dataset.Irritability=le.fit_transform(dataset.Irritability)
dataset.Delayed=le.fit_transform(dataset.Delayed)
dataset.Partial=le.fit_transform(dataset.Partial)
dataset.Muscle=le.fit_transform(dataset.Muscle)
dataset.Alopecia=le.fit_transform(dataset.Alopecia)
dataset.Obesity=le.fit_transform(dataset.Obesity)
dataset.Clase=le.fit_transform(dataset.Clase)

#Descripcion estadistica
dataset.describe()

#Informacion del set de datos
dataset.info()

#separar las variables con iloc ya que es más rapido que el drop
X=dataset.iloc[:,0:16].values
y=dataset.iloc[:,16].values

#dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

#Criterio entropy, (mide el desorden de incertidumbre, entropia alta = todos los datos estan revueltos, 
#entropia baja = los datos estan ordenados)
# Esta variable me ayuda a separar mejor los datos?
# Usa la media de los datos que mejor ordene y separe los datos
# max_depth limita la profundidad del arbol: nivel 1=raíz, nivel 2=primera division, nivel 3=segunda division, etc
modelo = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=0)
modelo.fit(X_train, y_train)

#Predicciones
y_pred = modelo.predict(X_test)
#Evaluacion del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#Matriz de confusion
matriz_confusion = confusion_matrix(y_test, y_pred)
print("Matriz de confusion|Accuracy:", matriz_confusion)
#matriz_confusion



#Graficar el arbol
plt.figure(figsize=(20,10))
tree.plot_tree(modelo, feature_names=list(dataset.drop(['Clase'], axis=1)), class_names=['No Diabetes', 'Diabetes'], filled=True)
#plot_tree(model, filled=True, feature_names=dataset.columns[0:16], class_names=model.classes_)
plt.show()
