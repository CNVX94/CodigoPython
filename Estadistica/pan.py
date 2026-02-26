import pandas as pd

datos = {
    "Nombre" : ["Ana", "Luis", "Maria", "Juan"],
    "Edad" : [20, 22, 19, 21],
    "Calificacion" : [85, 90, 78, 88]
}

df = pd.DataFrame(datos)    
print(df)   
print("Media de edad:", df["Edad"].mean())
print("Mediana de edad:", df["Edad"].median())
print("Moda de edad:", df["Edad"].mode()[0])

#Promedio de calificaciones

print("Media de calificaciones:", df["Calificacion"].mean())
print("Mediana de calificaciones:", df["Calificacion"].median())
print("Moda de calificaciones:", df["Calificacion"].mode()[0])

