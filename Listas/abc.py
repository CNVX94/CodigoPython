Abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Eliminar elemntos multiplos de 3

for i in range(len(Abc)-1, -1, -1):
    if (i+1) % 3 == 0:
        del Abc[i]
print(Abc)

#Conteo de vocales

while True:
    palabra = input("Ingresa una palabra (o 'salir' para terminar): ")
    if palabra.lower() == 'salir':
        break

    contador_vocales = 0
    for letra in palabra:
        if letra.lower() in 'aeiou':
            contador_vocales += 1

    print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")

    