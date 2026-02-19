
def calcularIva(salario):
    iva = salario * 0.21
    return iva

edad = input("Ingrese su edad: ")

if edad.isdigit():
    edad = int(edad)
    if edad < 18:
        print("Eres menor de edad.")
        print("Aún no pagas impuestos.")
    elif 18 <= edad < 65:
        print("Eres adulto.")
        salario = input("Ingrese su salario mensual: ")
        if salario.isdigit():
            salario = float(salario)
            if salario > 3000:
                iva = calcularIva(salario)
                print(f"Debes pagar impuestos. El IVA es de: ${iva:.2f}")
            else:
                print("No debes pagar impuestos.")
    else:
        print("Eres adulto mayor.")
        print("Jubilado, no pagas impuestos.")
else:
    print("Entrada no válida. Por favor ingrese un número.")

while True:
    frase = input("Ingrese una frase (o 'salir' para terminar): ")
    if frase.lower() == "salir":
        print("Programa terminado.")
        break
    else:
        frase = frase.lower()
        letra = input("Ingrese una letra para contar su frecuencia en la frase: ").lower()
        if len(letra) == 1 and letra.isalpha():
            frecuencia = frase.count(letra)
            print(f"La letra '{letra}' aparece {frecuencia} veces en la frase.")
        else:            
            print("Entrada no válida. Por favor ingrese una sola letra.")
        