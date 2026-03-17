import matplotlib.pyplot as plt

# Se tiene un conjunto de datos que representa el número de estudiantes que aprobaron un curso de matemáticas en 6 semestres consecutivos. 

semestres = ["2022-1", "2022-2", "2023-1", "2023-2", "2024-1", "2024-2"]
aprobados = [180, 90, 100, 200, 150, 180]

# Gráfico que muestra el número de estudiantes aprobados por semestre
plt.figure(figsize=(10, 6))
plt.bar(semestres, aprobados)
# SObreponer gráfico de líneas
plt.plot(semestres, aprobados, marker='o', linestyle='-', color='r')
# Mostrar cuadricula en el gráfico
plt.grid(True)
plt.xlabel("Semestres")
plt.ylabel("Número de estudiantes aprobados")
plt.title("Aprobación de estudiantes en cursos de matemáticas")
plt.show()
