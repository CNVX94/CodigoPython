
from Auto import Vehiculo

auto1 = Vehiculo("Toyota", "Corolla", "Rojo", 0)

# Menu con opciones.

salida = False

while not salida:
    print("¿Qué quieres hacer?")
    print("1. Mostrar información del auto")
    print("2. Acelerar el auto")
    print("3. Frenar el auto")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        auto1.mostrar_info()
    elif opcion == "2":
        incremento = int(input("¿Cuánto quieres acelerar? (km/h): "))
        auto1.acelerar(incremento)
    elif opcion == "3":
        decremento = int(input("¿Cuánto quieres frenar? (km/h): "))
        auto1.frenar(decremento)
    elif opcion == "4":
        salida = True
        print("¡Hasta luego!")
    else:
        print("Opción no válida, por favor ingresa un número del 1 al 4.")
