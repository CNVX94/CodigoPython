
from cajero import Cajero

nombre = input("Ingrese el nombre del titular de la cuenta: ")
cajero = Cajero(nombre, 0)

while True:
    
    print("\nSeleccione una opción:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cajero.depositar(cantidad)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cajero.retirar(cantidad)
    elif opcion == "3":
        cajero.consultar_saldo()
    elif opcion == "4":
        print("Gracias por usar el sistema bancario. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")