# Dada una lista de números enteros, realizar las siguientes operaciones

numeros = [5, 10, 15, 20, 25]

# Agregar un nuevo número a la lista

numeros.append(55)

# Eliminar un número de la lista

numeros.remove(10)

# Ordenar en forma ascendente

numeros.sort()

# Ordenar en forma descendente

numeros.reverse()

# Calcular promedio de los números

prom = sum(numeros) / len(numeros)
print(f"El promedio de los números es: {prom}")

# Numero mayor y numero menor

num_mayor = max(numeros)
num_menor = min(numeros)

print(f"El número mayor es: {num_mayor}")
print(f"El número menor es: {num_menor}")
