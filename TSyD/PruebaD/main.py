import usuario

while True:
    print("1. Consultar usuario por DNI")
    print("2. Agregar nuevo usuario")
    print("3. Eliminar usuario")
    print("4. Actualizar usuario")
    print("5. Mostrar todos los usuarios")
    print("6. Usuarios preferentes")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dni = input("Ingrese el DNI del usuario: ")
        usuario_info = usuario.obtener_usuario(dni)

        if usuario_info:
            print(f"Nombre: {usuario_info.nombre}")
            print(f"Dirección: {usuario_info.direccion}")
            print(f"Teléfono: {usuario_info.telefono}")
            print(f"Correo: {usuario_info.correo}")
            print(f"Preferente: {'Sí' if usuario_info.preferente else 'No'}")
            
    elif opcion == "2":
        print("Ingrese los datos del nuevo usuario:")
        dni = input("DNI: ")
        if dni in usuario.datos.bdcliente:
            print("El DNI ya existe. No se puede agregar el usuario.")
            continue
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        preferente_input = input("¿Es un cliente preferente? (sí/no): ")
        preferente = preferente_input.lower() == "sí"
        usuario.agregar_usuario(dni, nombre, direccion, telefono, correo, preferente)
        print("Usuario agregado exitosamente.")

    elif opcion == "3":
        dni = input("Ingrese el DNI del usuario a eliminar: ")
        usuario.eliminar_usuario(dni)

    elif opcion == "4":
        dni = input("Ingrese el DNI del usuario a actualizar: ")
        nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
        direccion = input("Ingrese la nueva dirección (deje en blanco para no cambiar): ")
        telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
        correo = input("Ingrese el nuevo correo (deje en blanco para no cambiar): ")
        preferente_input = input("¿Es un cliente preferente? (sí/no/dejar en blanco para no cambiar): ")
        preferente = None
        if preferente_input.lower() == "sí":
            preferente = True
        elif preferente_input.lower() == "no":
            preferente = False
        usuario.actualizar_usuario(dni, nombre or None, direccion or None, telefono or None, correo or None, preferente)
    
    elif opcion == "5":
        print("Usuarios registrados:")
        for dni, info in usuario.datos.bdcliente.items():
            print(f"- {info['nombre']} (DNI: {dni})")
    
    elif opcion == "6":
        usuario.usuarios_preferentes()
    
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor seleccione una opción válida.")
