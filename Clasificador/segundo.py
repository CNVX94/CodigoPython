## Código Python - Clasificador de Comentarios (Estructura Completa)
import tkinter as tk
from tkinter import ttk, scrolledtext

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto ML + Gemini | Clasificador de Comentarios")
        self.root.geometry("950x700")
        self.root.config(bg="#f4f6f8")

        # Crea una instancia del clasificador
        self.clasificador = ClasificadorComentarios()

        # Guarda el dataset base
        self.crear_dataset()

        # Construye la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Título principal
        titulo = tk.Label(
            self.root,
            text="Clasificador de Comentarios Estudiantiles",
            font=("Arial", 18, "bold"),
            bg="#f4f6f8",
            fg="#1f2d3d"
        )
        titulo.pack(pady=10)

        # Etiqueta secundaria descriptiva
        subtitulo = tk.Label(
            self.root,
            text="Machine Learning con scikit-learn + explicación con Gemini",
            font=("Arial", 11),
            bg="#f4f6f8",
            fg="#445566"
        )
        subtitulo.pack(pady=10)
    #Frame principal que contendrá el resto de componentes
        frame = tk.Frame(self, root, bg="#f4f6f8")
        frame.pack(fill="both", expand=True, padx=15, pady=10)
        # Etiqueta para caja de entrada
        lbl_texto = tk.Label(
            frame,
            text="Escribe un comentario:",
            font=("Arial", 12, "bold"),
            bg="#f4f6f8",
         ) 
        lbl_texto.pack(anchor="w")
        #Caja de texto de entrada con scroll
        self.txt_entrada = scrolledtext.ScrolledText(
            frame,
            height=6,
            font=("Arial", 11)
        )
    # Frame para organizar los botones.
    frame_botones = tk.Frame(frame, bg="#f4f6f8")
    frame_botones.pack(fill="x", pady=5)
    # Botón para entrenar el modelo
    btn_entrenar = ttk.Button(frame_botones, text="Entrenar modelo",
                              command=self.entrenar_modelo)
    btn_entrenar.grid(row=0, column=0, pax=5, pady=5)
    # Botón para predecr la clase del comentario
    btn_predecir = ttk.Button(frame_botones, text="Predecir",
                              command=self.predecir_texto)
    btn_predecir.grid(row=0, column=1, pax=5, pady=5)
    # Botón para pedir explicación a gemini
    btn_gemini = ttk.Button(frame_botones, text="Explicar con Gemini",
                              command=self.explicar_texto)
    btn_gemini.grid(row=0, column=2, pax=5, pady=5)
    # Botón para cargar un texto de ejemplo
    btn_ejemplo = ttk.Button(frame_botones, text="Cargar ejemplo",
                              command=self.cargar_ejemplo)
    btn_entrenar.grid(row=0, column=3, pax=5, pady=5)
    #Boton para limpiar todas las áreas
                              command=self.entrenar_modelo)
    btn_entrenar.grid(row=0, column=0, pax=5, pady=5)
#             frame,
#             text="Escribe un comentario:",
            


#         self.txt_entrada.pack(fill="x", pady=5)

#         # Frame de botones
#         frame_botones = tk.Frame(frame, bg="#f4f6f8")
#         frame_botones.pack(fill="x", pady=10)

#         # Botón entrenar
#         btn_entrenar = ttk.Button(
#             frame_botones,
#             text="Entrenar modelo",
#             command=self.entrenar_modelo
#         )
#         btn_entrenar.pack(side="left", padx=5)

#         # Botón clasificar
#         btn_clasificar = ttk.Button(
#             frame_botones,
#             text="Clasificar comentario",
#             command=self.clasificar_comentario
#         )
#         btn_clasificar.pack(side="left", padx=5)

#         # Área de resultado
#         self.lbl_resultado = tk.Label(
#             frame,
#             text="Resultado:",
#             font=("Arial", 12),
#             bg="#f4f6f8",
#             fg="#1f2d3d"
#         )
#         self.lbl_resultado.pack(pady=10)

#     # Métodos base (estructura)
#     def crear_dataset(self):
#         pass

#     def entrenar_modelo(self):
#         pass

#     def clasificar_comentario(self):
#         pass


# # Ejecución de la app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
