class Libro:
    def __init__(self): #Argumentos.
        #Atributos del objeto de la clase libro
        #self hace refrencia al objeto como tal
        self.id = "12345"
        self.titulo = "Supremacia Cuantica" # Como visualizan el futuro en cuestiónes cuanticas
        self.autor = "Michio Kaku"
        self.publicacion = "2004"
        self.disponible = True
        #Metodos: Acciones que se puden realizar, una de ellas será ver la información del objeto.
    def mostrarInformacion(self,id): # el sistema va a secir, ¿Qué quieres hacer?
        self.id = id
        if self.id == "12345":
            print(f"Titulo: {self.titulo}, Autor:{self.autor}, Año: {self.publicacion}, Disponible :{self.disponible}")#Concatenación con texto fijo
        else:
            print("El código no existe")
    def prestarLibro(self,id):
        self.id = id
        if self.id == "12345":
            if self.disponible:
                print("El libro se puede prestar")
                self.disponible = False
            else:
                print("Libro no disponible")

    def devolverLibro(self,id):
        self.id = id
        if self.id == "12345":
            if not self.disponible:
                print("El libro se ha devuelto")
                self.disponible = True
            else:
                print("El libro ya está disponible")    

