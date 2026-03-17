# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:28:21 2026

@author: desarrollo 6
"""

from tkinter import *

def mensaje():
    print("Obediente")

# Crear ventana
ventana= Tk()
# Titulo de la ventana
ventana.title("Ventana de pruebas:")
# Redimensionar
ventana.resizable(True, False)
# Tamaño
ventana.geometry("650x350")
# Diseño
ventana.config(bg="blue")
# Se puede añadir mediante codigo hexadecimal}
# ventana.config(bg="#5676E8")
# Colocar etiquetas
lbl=Label(ventana, text="Hola Mundo")
# Clase pack
lbl.pack()
lbl2=Label(ventana, text="Hola Mundo")
lbl2.pack()
# Boton, command requiere de una funcion
btn=Button(ventana, text="Presionar botón", command=mensaje)
btn.pack()
# Edicion en el objeto
btn2=Button(ventana, text="Presionar botón", 
            bg="pink", fg="green", command=mensaje)
btn2.pack()
# Config
btn3 = Button(ventana, text="Tercer boton",
              command=mensaje)
btn3.config(fg="blue", bg="green")
btn3.pack()
# Clave valor
btn4 = Button(ventana, text="Tercer boton",
              command=mensaje)
btn4["fg"]="red"
btn4["bg"]="pink"
btn4.pack()
ventana.mainloop()
