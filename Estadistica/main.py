
from random import random

from estadistica import Estadistica

lista_numeros = [2,4,6,8,4,6,4]

Estadistica = Estadistica(lista_numeros)

print ("Media:", Estadistica.calcular_media())
print ("Mediana:", Estadistica.calcular_mediana())
print ("Moda:", Estadistica.calcular_moda())

