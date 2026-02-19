
print("Hola")

# Lista

Lista=[1,2,3,4,"Mayte",[True,False,True]]

print(Lista)

#Acceder lista

print(Lista[0])

#Acceder a más de un indice

print(Lista[0:4])

#

print(Lista[3:])

#Indice negativo

print(Lista[-2])

print(Lista[-3:])

#Doble referencia

print(Lista[5][1])

print(Lista[-1][-2:])

Lista[0] = 10

print(Lista[0])

#Append, agrega al úlitmo indice el valor

Lista.append([5])

#Flotantes

Lista.append([3.43])

print(Lista)

Lista2=[1,2]

Lista2.extend([3,4,True])

print(Lista2)
#Extiende la lista, agregar varios datos al mismo tiempo
Lista2.insert(0,"y")
print(Lista2)

x=[1,2,3]

del x[1]

y=[4,5,6,7,8]
print(y)
del y[:2]

print(y)

z=[1,2,"h",3,"h"]

z.remove("h")

r=[4,6,1,3,2]
r.reverse()
print(z)
r.sort()
print(z)

x3=[10,30,20]
print(x3.index(30))

nombre=["Mayte", "Rosa", "Raul"]

print(nombre.count("Mayte"))

# Ejercicio: pedir notas de materias y mostrarlas

materias = ["Matemáticas", "IA", "IO", "AMov", "AW"]
notas = []

for materia in materias:
    while True:
        nota_str = input(f"Agrega tu calificación de {materia}: ")
        try:
            nota = float(nota_str)  # Convertimos a número (admite decimales)
            if 0 <= nota <= 10:     # Validación básica (opcional)
                notas.append(nota)
                break
            else:
                print("⚠️ La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")

print("\n📋 Notas registradas:")
for materia, nota in zip(materias, notas):
    print(f"{materia}: {nota}")

# Opcional: calcular y mostrar el promedio
if notas:
    promedio = sum(notas) / len(notas)
    print(f"\n📈 Promedio general: {promedio:.2f}")
        