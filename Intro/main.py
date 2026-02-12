# Verificar si un número es par o impar
print("Verificar si un número es par o impar:")
num1 = int(input("Introduce el número a verificar: "))
if num1 % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Verificar si es positivo, negativo o cero

print("Verificar si un número es positivo, negativo o cero:")
num2= int(input("Introduce el número a verificar: "))

if num2 > 0:
    print("El número es positivo.")
elif num2 < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Comprobar mayoria de edad

num3 = int(input("Introduce tu edad: "))

if num3 >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Materia aprobada o reprobada

num4 = int(input("Introduce tu calificación: "))

if num4 >= 60:
    print("Has aprobado la materia.")
else:
    print("Has reprobado la materia.")
    
# Califiación (Letras A, B, C, D, F)

num5 = int(input("Introduce tu calificación: "))

if num5 >= 90:
    print("Tu calificación es A.")
elif num5 >= 80:
    print("Tu calificación es B.")
elif num5 >= 70:
    print("Tu calificación es C.")
elif num5 >= 60:
    print("Tu calificación es D.")
else:
    print("Tu calificación es F.")
    
# Determinar el estado del agua según la temperatura.

num6 = float(input("Introduce la temperatura del agua en grados Celsius: "))

if num6 <= 0:
    print("El agua está congelada.")
elif num6 >= 100:
    print("El agua está hirviendo.")
else:
    print("El agua está en estado líquido.")
