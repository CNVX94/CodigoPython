from rectangulo import Rectangulo

# Crear un objeto Rectangulo

input_ancho = float(input("Ingrese el ancho del rectángulo: "))
input_alto = float(input("Ingrese el alto del rectángulo: "))

mi_rectangulo = Rectangulo(input_ancho, input_alto)

# Mostrar la información del rectángulo

mi_rectangulo.mostrar_informacion()

