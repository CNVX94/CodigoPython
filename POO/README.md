Registro de libros.

Si lo puedo prestar, si no, información de los objetos que tenga yo ahi

# Crear un sistema para gesrionar una biblioteca con las siguientes clases, Libro, usuario y biblioteca.

## libros.py

~~~python

class Libro:
    def __init__(self): #Argumentos.
        #Atributos del objeto de la clase libro
        #self hace refrencia al objeto como tal
        self.id = "12345"
        self.titulo = "Supremacia Cuantica" # Como visualizan el futuro en cuestiónes cuanticas
        self.autor = "Michio Kaku"
        self.publicacion = "2004"
        self.disponible = True

        #Metodos: Acciones que se puden realizar, una de ellas será ver la información del objeto.
        def mostrarInformacion(self,id): # el sistema va a secir, ¿Qué quieres hacer?
            self.id = id
            if self.id == "12345":
                print(f"Titulo: {self.titulo}", "Autor:"{self.autor}, "Año: "{self.publicacion}, "Disponible :"{self.disponible})#Concatenación con texto fijo
            else
                print("El código no existe")

~~~

## index.py 

Importar la clase, metodos que voy a estar escribiendo.

~~~python

from libros import Libro

mi_libro = Libro()

mi_libro.mostrarInformacion("12345")


~~~

~~~bash

python index.py

~~~

## Prestamo

## libros.py
~~~python


# Dentro de class Libro:

    def prestarLibro(self,id):
        self.id = id
        if self.id == "12345":
            if self.disponible:
                print("El libro se puede prestar")
                self.disponible = False
            else:
                print("Libro no disponible")



~~~

## index.py

Menu repetitivo con ciclo while

~~~Python

salida = False

while not salida:
    print("¿Qué quieres hacer?")
    print("1. Mostrar información del libro")
    print("2. Prestar el libro")
    print("3. Devolver el libro")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        mi_libro.mostrarInformacion("12345")
    elif opcion == "2":
        mi_libro.prestarLibro("12345")
    elif opcion == "3":
        mi_libro.devolverLibro("12345")
    elif opcion == "4":
        salida = True
        print("¡Hasta luego!")
    else:
        print("Opción no válida, por favor ingresa un número del 1 al 4.")
        

~~~