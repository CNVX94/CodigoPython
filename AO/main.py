
lista = [5,7,3,1,8,4,9,2,6]

longitud = len(lista)

for i in range(longitud-1):
    indice_menor=i
    for j in range(i+1,longitud):
        if lista[j] < lista[indice_menor]:
            indice_menor=j

    temporal = lista[indice_menor]
    lista[indice_menor] = lista[i]
    lista[i] = temporal

print("Lista ordenada:", lista)

## Selection Sort

## Busca el elemento más pequeño no ordenado y lo intercambia con
## el elemento en la posición correcta.