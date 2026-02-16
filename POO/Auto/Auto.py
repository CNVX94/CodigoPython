
class Vehiculo:
    def __init__ (self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad

    def acelerar(self, incremento):
            self.velocidad += incremento
            print(f"El vehículo ha acelerado. Velocidad actual: {self.velocidad} km/h")

    def frenar(self, decremento):
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            print(f"El vehículo ha frenado. Velocidad actual: {self.velocidad} km/h")

    def mostrar_info(self):
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Color: {self.color}")
            print(f"Velocidad: {self.velocidad} km/h")

