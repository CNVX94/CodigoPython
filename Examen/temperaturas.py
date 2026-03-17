import numpy as np

# Se tiene un conjunto de datos de temperaturas (en grados Celsius) de 7 ciudades durante 7 días almacenado en una matriz 7x7 generada aleatoriamente entre -5°C y 40°C. Se deben realizar las siguientes operaciones utilizando NumPy:

# Generar la matriz de temperaturas
temperaturas = np.random.randint(-5, 40, size=(7, 7))
# Mostrar la matriz
print("Matriz de temperaturas (°C):")
print(temperaturas)

# Caclular la temperatura promedio de cada ciudad (filas)

promedio_ciudades = np.mean(temperaturas, axis=1)
print("Promedio de temperaturas por ciudad (°C):")
print(promedio_ciudades)

# Obtener la temperatura máxima por fila

temp_max_ciudad = np.max(temperaturas, axis=1)
temp_max_error = np.argmax(temperaturas, axis=1) + 1
print("Temperatura máxima por ciudad (°C):")
print(temp_max_ciudad)
print("Día de la temperatura máxima por ciudad (0-6):")
print(temp_max_error)

# Convertir a grados Fahrenheit

# Fórmula: F = C * 9/5 + 32
# Prueba a mano
print("Prueba de conversión de temperatura a mano:")
tC = 25
tF = tC * 9/5 + 32
print(f"{tC}°C es igual a {tF}°F")

temp_farenheit = temperaturas * 9/5 + 32
print("Matriz de temperaturas en grados Fahrenheit (°F):")  
print(temp_farenheit)