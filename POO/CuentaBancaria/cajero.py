
class Cajero:
    def __init__ (self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes. Retiro no permitido.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
    
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")