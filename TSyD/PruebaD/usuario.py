import datos

class Usuario:
    def __init__ (self, nombre, direccion, telefono, correo, preferente):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.preferente = preferente

def obtener_usuario(dni):
    if dni in datos.bdcliente:
        info = datos.bdcliente[dni]
        return Usuario(info["nombre"], info["direccion"], info["telefono"], info["correo"], info["preferente"])
    else:
        print("Usuario no encontrado.")
        return None

def agregar_usuario(dni, nombre, direccion, telefono, correo, preferente):
    if dni not in datos.bdcliente:
        datos.bdcliente[dni] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }
        print("Usuario agregado exitosamente.")
    else:
        print("El DNI ya existe. No se puede agregar el usuario.")

def eliminar_usuario(dni):
    if dni in datos.bdcliente:
        del datos.bdcliente[dni]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado. No se puede eliminar.")

def actualizar_usuario(dni, nombre=None, direccion=None, telefono=None, correo=None, preferente=None):
    if dni in datos.bdcliente:
        if nombre is not None:
            datos.bdcliente[dni]["nombre"] = nombre
        if direccion is not None:
            datos.bdcliente[dni]["direccion"] = direccion
        if telefono is not None:
            datos.bdcliente[dni]["telefono"] = telefono
        if correo is not None:
            datos.bdcliente[dni]["correo"] = correo
        if preferente is not None:
            datos.bdcliente[dni]["preferente"] = preferente
        print("Usuario actualizado exitosamente.")
    else:
        print("Usuario no encontrado. No se puede actualizar.")

def usuarios_preferentes():
    preferentes = [dni for dni, info in datos.bdcliente.items() if info["preferente"]]
    if preferentes:
        print("Usuarios preferentes:")
        for dni in preferentes:
            print(f"- {datos.bdcliente[dni]['nombre']} (DNI: {dni})")
    else:
        print("No hay usuarios preferentes.")