class Estadistica:
    def __init__ (self, mumeros):
        self.numeros = mumeros

    def calcular_media(self):
        #return sum(self.numeros) / len(self.numeros)
        suma = sum(self.numeros) / len(self.numeros)
        return suma
    
    def calcular_mediana(self):
        numeros_ordenados = sorted(self.numeros)
        n = len(numeros_ordenados)
        mitad = n//2 # Division entera para obtener el índice de la mitad
        if n % 2 == 0: # Si el número de elementos es par, se promedian los dos elementos centrales
            mediana = (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else: # Si el número de elementos es impar, se toma el elemento central
            mediana = numeros_ordenados[mitad]
        return mediana
    
    def calcular_moda(self):
        frecuencia = {}
        for numro in self.numeros: #Recorre la lista de números y cuenta la frecuencia de cada número
            if numro in frecuencia:
                frecuencia[numro] += 1
            else:
                frecuencia[numro] = 1
        max_frecuencia = max(frecuencia.values())
        modas = []
        
        for numro, freq in frecuencia.items(): #Recorre el diccionario de frecuencias y encuentra los números que tienen la frecuencia máxima
            if freq == max_frecuencia:
                modas.append(numro) # Agrega el número a la lista de modas si su frecuencia es igual a la frecuencia máxima
            if len(modas) == len(self.numeros): # Si todos los números tienen la misma frecuencia, no hay moda
                return None
        #moda = max(frecuencia, key=frecuencia.get) # Encuentra el número con la mayor frecuencia
        return modas
     

    
