# -*- coding: utf-8 -*-
"""
Visualizador de Actividades - Aplicación Tkinter
Permite visualizar y ejecutar archivos Python del directorio
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog, filedialog
import os
import subprocess
import sys


class VisualizadorActividades:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Actividades")
        self.root.geometry("900x600")
        
        self.directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivos = []
        self.archivo_seleccionado = None
        
        self.crear_menu()
        self.crear_interfaz()
        self.cargar_archivos()
    
    def crear_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Cambiar Carpeta", command=self.cambiar_carpeta)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        
        # Menú Actividades
        menu_actividades = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Actividades", menu=menu_actividades)
        menu_actividades.add_command(label="Ejecutar Archivo", command=self.ejecutar_archivo, accelerator="F5")
        menu_actividades.add_separator()
        menu_actividades.add_command(label="Actualizar Lista", command=self.cargar_archivos)
        
        # Menú Gráficas
        menu_graficas = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Gráficas", menu=menu_graficas)
        menu_graficas.add_command(label="Editar Semestres", command=self.editar_semestres)
        menu_graficas.add_command(label="Editar Aprobados", command=self.editar_aprobados)
        menu_graficas.add_separator()
        menu_graficas.add_command(label="Ver Gráfico", command=self.ver_grafico)
        
        # Binding para F5
        self.root.bind('<F5>', lambda e: self.ejecutar_archivo())
    
    def crear_interfaz(self):
        # Paneles principales
        panel_principal = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        panel_principal.pack(fill=tk.BOTH, expand=True)
        
        # Panel izquierdo - Lista de archivos
        panel_izquierdo = ttk.Frame(panel_principal)
        panel_principal.add(panel_izquierdo, weight=1)
        
        # Etiqueta y lista
        lbl_titulo = ttk.Label(panel_izquierdo, text="Archivos Python", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=5)
        
        self.lista_archivos = tk.Listbox(panel_izquierdo, font=("Courier", 10))
        self.lista_archivos.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.lista_archivos.bind('<<ListboxSelect>>', self.al_seleccionar_archivo)
        
        # Panel derecho - Contenido
        panel_derecho = ttk.Frame(panel_principal)
        panel_principal.add(panel_derecho, weight=3)
        
        lbl_contenido = ttk.Label(panel_derecho, text="Contenido del Archivo", font=("Arial", 12, "bold"))
        lbl_contenido.pack(pady=5)
        
        self.texto_contenido = scrolledtext.ScrolledText(panel_derecho, font=("Courier", 10), wrap=tk.NONE)
        self.texto_contenido.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.texto_contenido.config(state=tk.DISABLED)
        
        # Scrollbar horizontal para el texto
        scrollbar_h = ttk.Scrollbar(panel_derecho, orient=tk.HORIZONTAL, command=self.texto_contenido.xview)
        scrollbar_h.pack(fill=tk.X, side=tk.BOTTOM)
        self.texto_contenido.config(xscrollcommand=scrollbar_h.set)
        
        # Panel inferior - Botones
        panel_inferior = ttk.Frame(self.root)
        panel_inferior.pack(fill=tk.X, padx=10, pady=5)
        
        btn_ejecutar = ttk.Button(panel_inferior, text="Ejecutar (F5)", command=self.ejecutar_archivo)
        btn_ejecutar.pack(side=tk.LEFT, padx=5)
        
        btn_carpeta = ttk.Button(panel_inferior, text="Cambiar Carpeta", command=self.cambiar_carpeta)
        btn_carpeta.pack(side=tk.LEFT, padx=5)
        
        self.lbl_ruta = ttk.Label(panel_inferior, text=f"Carpeta: {self.directorio_actual}", foreground="gray")
        self.lbl_ruta.pack(side=tk.RIGHT, padx=5)
    
    def cargar_archivos(self):
        self.lista_archivos.delete(0, tk.END)
        self.archivos = []
        
        try:
            for archivo in os.listdir(self.directorio_actual):
                if archivo.endswith('.py') and archivo != '__pycache__':
                    self.archivos.append(archivo)
                    self.lista_archivos.insert(tk.END, archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la carpeta: {e}")
    
    def cambiar_carpeta(self):
        carpeta = filedialog.askdirectory(initialdir=self.directorio_actual)
        if carpeta:
            self.directorio_actual = carpeta
            self.lbl_ruta.config(text=f"Carpeta: {self.directorio_actual}")
            self.texto_contenido.config(state=tk.NORMAL)
            self.texto_contenido.delete(1.0, tk.END)
            self.texto_contenido.config(state=tk.DISABLED)
            self.cargar_archivos()
    
    def al_seleccionar_archivo(self, event):
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            indice = seleccion[0]
            self.archivo_seleccionado = self.archivos[indice]
            self.mostrar_contenido(self.archivo_seleccionado)
    
    def mostrar_contenido(self, nombre_archivo):
        ruta_archivo = os.path.join(self.directorio_actual, nombre_archivo)
        
        self.texto_contenido.config(state=tk.NORMAL)
        self.texto_contenido.delete(1.0, tk.END)
        
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            self.texto_contenido.insert(1.0, contenido)
        except Exception as e:
            self.texto_contenido.insert(1.0, f"Error al leer el archivo: {e}")
        
        self.texto_contenido.config(state=tk.DISABLED)
    
    def ejecutar_archivo(self):
        if not self.archivo_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un archivo para ejecutar")
            return
        
        respuesta = messagebox.askyesno("Confirmar", f"¿Desea ejecutar {self.archivo_seleccionado}?")
        if respuesta:
            ruta_archivo = os.path.join(self.directorio_actual, self.archivo_seleccionado)
            
            try:
                messagebox.showinfo("Ejecutando", f"Ejecutando {self.archivo_seleccionado}...\n(Consulte la consola para ver la salida)")
                resultado = subprocess.run(
                    [sys.executable, ruta_archivo],
                    capture_output=True,
                    text=True,
                    cwd=self.directorio_actual
                )
                
                if resultado.stdout:
                    messagebox.showinfo("Salida", resultado.stdout)
                if resultado.stderr:
                    messagebox.showerror("Error", resultado.stderr)
                    
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo ejecutar el archivo: {e}")
    
    def editar_semestres(self):
        ruta_graficos = os.path.join(self.directorio_actual, "graficos.py")
        
        if not os.path.exists(ruta_graficos):
            messagebox.showerror("Error", "No se encontró graficos.py")
            return
        
        semestres_actuales = ["2020-1", "2020-2", "2021-1", "2021-2", "2022-1", "2022-2"]
        nuevo_semestre = simpledialog.askstring("Editar Semestres", 
            "Ingrese los semestres separados por coma:\n(Actualmente: " + ", ".join(semestres_actuales) + ")")
        
        if nuevo_semestre:
            semestres_lista = [s.strip() for s in nuevo_semestre.split(",") if s.strip()]
            if semestres_lista:
                self.modificar_graficos(semestres=semestres_lista)
            else:
                messagebox.showerror("Error", "Debe ingresar al menos un semestre")
    
    def editar_aprobados(self):
        ruta_graficos = os.path.join(self.directorio_actual, "graficos.py")
        
        if not os.path.exists(ruta_graficos):
            messagebox.showerror("Error", "No se encontró graficos.py")
            return
        
        aprobados_actuales = [120, 150, 180, 160, 200, 220]
        nuevos_aprobados = simpledialog.askstring("Editar Aprobados",
            "Ingrese los números de aprobados separados por coma:\n(Actualmente: " + str(aprobados_actuales)[1:-1] + ")")
        
        if nuevos_aprobados:
            try:
                aprobados_lista = [int(a.strip()) for a in nuevos_aprobados.split(",") if a.strip()]
                if aprobados_lista:
                    self.modificar_graficos(aprobados=aprobados_lista)
                else:
                    messagebox.showerror("Error", "Debe ingresar al menos un número")
            except ValueError:
                messagebox.showerror("Error", "Debe ingresar solo números separados por coma")
    
    def modificar_graficos(self, semestres=None, aprobados=None):
        ruta_graficos = os.path.join(self.directorio_actual, "graficos.py")
        
        try:
            with open(ruta_graficos, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            if semestres:
                semestres_str = str(semestres).replace("'", '"')
                lineas = contenido.split('\n')
                contenido_nuevo = []
                for linea in lineas:
                    if 'semestres = [' in linea:
                        contenido_nuevo.append(f'semestres = {semestres_str}')
                    else:
                        contenido_nuevo.append(linea)
                contenido = '\n'.join(contenido_nuevo)
            
            if aprobados:
                aprobados_str = str(aprobados)
                lineas = contenido.split('\n')
                contenido_nuevo = []
                for linea in lineas:
                    if 'aprobados = [' in linea:
                        contenido_nuevo.append(f'aprobados = {aprobados_str}')
                    else:
                        contenido_nuevo.append(linea)
                contenido = '\n'.join(contenido_nuevo)
            
            with open(ruta_graficos, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            messagebox.showinfo("Éxito", "Archivo graficos.py actualizado correctamente")
            
            if self.archivo_seleccionado == "graficos.py":
                self.mostrar_contenido("graficos.py")
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el archivo: {e}")
    
    def ver_grafico(self):
        self.archivo_seleccionado = "graficos.py"
        self.mostrar_contenido("graficos.py")
        
        respuesta = messagebox.askyesno("Confirmar", "¿Desea ejecutar graficos.py para ver el gráfico?")
        if respuesta:
            ruta_graficos = os.path.join(self.directorio_actual, "graficos.py")
            try:
                subprocess.Popen([sys.executable, ruta_graficos], cwd=self.directorio_actual)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo ejecutar el gráfico: {e}")


def main():
    root = tk.Tk()
    app = VisualizadorActividades(root)
    root.mainloop()


if __name__ == "__main__":
    main()
