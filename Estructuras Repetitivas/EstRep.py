# Suma de N numeros naturales usando un ciclo for

n = int(input("Ingrese un numero: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print("La suma de los primeros", n, "numeros naturales es:", suma)

# Factorial de un numero usando un ciclo for

num = int(input("Ingrese un numero para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("El factorial de", num, "es:", factorial)

# Tabla de multiplicar

num = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
print("Tabla de multiplicar del", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Cálculo del promedio de notas

num_notas = int(input("Ingrese el numero de notas: "))
suma_notas = 0
for i in range(num_notas):
    nota = float(input("Ingrese la nota " + str(i + 1) + ": "))
    suma_notas += nota
promedio = suma_notas / num_notas
print("El promedio de las notas es:", promedio)


# Potencia de un numero usando un ciclo for

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = 1
for i in range(exponente):
    resultado *= base
print(base, "elevado a la", exponente, "es:", resultado)    

# Suma de numeros pares en un rango

inicio = int(input("Ingrese el numero de inicio del rango: "))
fin = int(input("Ingrese el numero de fin del rango: "))
suma_pares = 0
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        suma_pares += i
print("La suma de los numeros pares entre", inicio, "y", fin, "es:", suma_pares)

