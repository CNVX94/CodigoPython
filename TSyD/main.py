## Tupla con los meses del año.
## Pide un número al usuario
## Si el numero esta enre 1 y la longitud máxima de la tupla
## muestra el contenido de esa posición, sino muestra un mensaje de error.}

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

num = int(input("Ingrese un número entre 1 y 12: "))
if 1 <= num <= len(meses):
    print(f"El mes correspondiente al número {num} es: {meses[num - 1]}")
else:
    print("Número fuera de rango. Por favor ingrese un número entre 1 y 12.")

## Almacenar los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre
## por pantalla su producto escalar.

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

producto_escalar = sum(a * b for a, b in zip(vector1, vector2))

print(f"El producto escalar de {vector1} y {vector2} es: {producto_escalar}")

## Almacenar creditos por materia y luego mostrarlas concatenadas.

materias = ["Matematicas", "IA", "IO", "AMov", "AW"]
  
notas = []

for materia in materias:
    nota = input("Agrega tu calificación de " + materia + ": ")
    notas.append(float(nota)) 
print(notas)

for i in materias:
    print(str(i) + " " + str(notas[materias.index(i)]))


        
        