import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from sklearn.linear_model import LogisticRegression
import random
import requests
import json

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "deepseek-v3.1:671b-cloud"

COLORS = {
    "bg_principal": "#1a1a2e",
    "bg_secundario": "#16213e",
    "bg_card": "#0f3460",
    "bg_input": "#1f4068",
    "acento": "#e94560",
    "acento_hover": "#ff6b6b",
    "texto_principal": "#ffffff",
    "texto_secundario": "#b8b8b8",
    "exito": "#00d9a5",
    "advertencia": "#ffc107",
    "error": "#ff4757",
    "borde": "#2a4a7a"
}

def generar_datos_simulados(n=200):
    np.random.seed(42)
    datos = []
    
    for _ in range(n):
        horas = random.randint(1, 20)
        asistencia = random.randint(50, 100)
        tareas = random.randint(0, 10)
        
        puntaje = 0.35 * horas + 0.08 * asistencia + 0.6 * tareas
        aprobo = 1 if puntaje >= 12 else 0
        
        datos.append([horas, asistencia, tareas, aprobo])
    
    return datos

def entrenar_modelo():
    datos = generar_datos_simulados(200)
    X = np.array([d[:3] for d in datos])
    y = np.array([d[3] for d in datos])
    
    modelo = LogisticRegression(random_state=42, max_iter=1000)
    modelo.fit(X, y)
    
    return modelo

modelo = entrenar_modelo()

def calcular_puntaje(horas, asistencia, tareas):
    return 0.35 * horas + 0.08 * asistencia + 0.6 * tareas

def predecir(modelo, horas, asistencia, tareas):
    X_nuevo = np.array([[horas, asistencia, tareas]])
    prediccion = modelo.predict(X_nuevo)[0]
    probabilidad = modelo.predict_proba(X_nuevo)[0][1]
    return prediccion, probabilidad

def generar_explicacion_ollama(horas, asistencia, tareas, puntaje, probabilidad, prediccion):
    try:
        resultado = "APRUEBA" if prediccion == 1 else "REPRUEBA"
        
        prompt = f"""Eres un asistente educativo. Un estudiante tiene los siguientes datos:
- Horas de estudio por semana: {horas}
- Porcentaje de asistencia: {asistencia}%
- Número de tareas entregadas: {tareas}

El puntaje calculado es: {puntaje:.2f}
La probabilidad de aprobación según el modelo es: {probabilidad:.2%}
El resultado predicho es: {resultado}

Genera una explicación pedagógica y personalizada para el estudiante, mencionando:
1. Qué factores están influyendo positivamente en su resultado
2. Qué podría mejorar para aprobar
3. Un mensaje motivacional

Sé breve y orientador."""
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json().get("response", "No se pudo generar la explicación")
        else:
            return f"Error de Ollama: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "Error: No se pudo conectar a Ollama. Asegúrate de que Ollama esté ejecutándose."
    except Exception as e:
        return f"Error al generar explicación: {str(e)}"

class StyledEntry(ttk.Entry):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(style="Styled.TEntry")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Predicción de Aprobación Estudiantil")
        self.root.geometry("700x800")
        self.root.configure(bg=COLORS["bg_principal"])
        
        self.entry_horas = None
        self.entry_asistencia = None
        self.entry_tareas = None
        self.lbl_puntaje = None
        self.lbl_regla = None
        self.lbl_prediccion = None
        self.lbl_probabilidad = None
        self.txt_explicacion = None
        
        self.setup_styles()
        self.create_widgets()
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure(".", background=COLORS["bg_principal"])
        style.configure("TFrame", background=COLORS["bg_principal"])
        style.configure("Card.TFrame", background=COLORS["bg_card"])
        
        style.configure("TLabel", 
                       background=COLORS["bg_principal"], 
                       foreground=COLORS["texto_principal"],
                       font=("Segoe UI", 11))
        
        style.configure("Header.TLabel", 
                       background=COLORS["bg_principal"], 
                       foreground=COLORS["texto_principal"],
                       font=("Segoe UI", 24, "bold"))
        
        style.configure("Subheader.TLabel", 
                       background=COLORS["bg_card"], 
                       foreground=COLORS["texto_secundario"],
                       font=("Segoe UI", 10))
        
        style.configure("Card.TLabelframe", 
                       background=COLORS["bg_card"], 
                       foreground=COLORS["texto_principal"],
                       borderwidth=0,
                       font=("Segoe UI", 12, "bold"))
        
        style.configure("Card.TLabelframe.Label", 
                       background=COLORS["bg_card"], 
                       foreground=COLORS["acento"],
                       font=("Segoe UI", 13, "bold"))
        
        style.configure("Result.TLabel",
                       background=COLORS["bg_card"],
                       foreground=COLORS["texto_principal"],
                       font=("Segoe UI", 12))
        
        style.configure("Styled.TEntry",
                       fieldbackground=COLORS["bg_input"],
                       foreground=COLORS["texto_principal"],
                       borderwidth=0,
                       insertcolor=COLORS["texto_principal"],
                       font=("Segoe UI", 12))
        
        style.map("Styled.TEntry",
                 fieldbackground=[("focus", COLORS["bg_input"])],
                 bordercolor=[("focus", COLORS["acento"])])
        
        style.configure("Accent.TButton",
                       background=COLORS["acento"],
                       foreground=COLORS["texto_principal"],
                       borderwidth=0,
                       font=("Segoe UI", 12, "bold"),
                       padding=(20, 10))
        
        style.map("Accent.TButton",
                 background=[("active", COLORS["acento_hover"])])
        
        style.configure("Secondary.TButton",
                       background=COLORS["bg_input"],
                       foreground=COLORS["texto_principal"],
                       borderwidth=1,
                       bordercolor=COLORS["borde"],
                       font=("Segoe UI", 11),
                       padding=(15, 8))
        
        style.map("Secondary.TButton",
                 background=[("active", COLORS["bg_card"])],
                 bordercolor=[("active", COLORS["acento"])])
        
        style.configure("Result.TText",
                       background=COLORS["bg_input"],
                       foreground=COLORS["texto_principal"],
                       borderwidth=0,
                       font=("Segoe UI", 11))
        
        style.configure("TSeparator",
                       background=COLORS["borde"])
    
    def create_widgets(self):
        main_container = ttk.Frame(self.root, style="TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        header_frame = ttk.Frame(main_container, style="TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 25))
        
        title = ttk.Label(header_frame, 
                         text="🎓", 
                         style="Header.TLabel",
                         font=("Segoe UI", 36))
        title.pack(side=tk.LEFT, padx=(0, 15))
        
        title_text = ttk.Frame(header_frame, style="TFrame")
        title_text.pack(side=tk.LEFT)
        
        ttk.Label(title_text, 
                 text="Predicción de Aprobación", 
                 style="Header.TLabel").pack(anchor=tk.W)
        
        ttk.Label(title_text, 
                 text="Ingresa los datos del estudiante para predecir su rendimiento académico",
                 style="Subheader.TLabel").pack(anchor=tk.W, pady=(5, 0))
        
        input_card = ttk.LabelFrame(main_container, 
                                    text="📊 Datos del Estudiante",
                                    style="Card.TLabelframe",
                                    padding=25)
        input_card.pack(fill=tk.X, pady=(0, 20))
        
        self.create_input_field(input_card, "⏱️ Horas de estudio semanal", "entry_horas", "1 - 20 horas")
        self.create_input_field(input_card, "📅 Porcentaje de asistencia", "entry_asistencia", "50% - 100%")
        self.create_input_field(input_card, "📝 Tareas entregadas", "entry_tareas", "0 - 10 tareas")
        
        btn_frame = ttk.Frame(main_container, style="TFrame")
        btn_frame.pack(fill=tk.X, pady=(0, 20))
        
        btn_predecir = ttk.Button(btn_frame, 
                                  text="✨ Realizar Predicción", 
                                  style="Accent.TButton",
                                  command=self.predecir)
        btn_predecir.pack(side=tk.LEFT, padx=(0, 10))
        
        btn_limpiar = ttk.Button(btn_frame, 
                                text="🔄 Limpiar", 
                                style="Secondary.TButton",
                                command=self.limpiar)
        btn_limpiar.pack(side=tk.LEFT)
        
        self.resultado_frame = ttk.LabelFrame(main_container, 
                                              text="📈 Resultados del Análisis",
                                              style="Card.TLabelframe",
                                              padding=20)
        self.resultado_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(self.resultado_frame, 
                          bg=COLORS["bg_card"],
                          highlightthickness=0)
        
        self.canvas = canvas
        
        scrollbar = ttk.Scrollbar(self.resultado_frame, 
                                 orient=tk.VERTICAL, 
                                 command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas, style="Card.TFrame")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=580)
        
        def on_canvas_configure(event):
            canvas.itemconfig(canvas_window, width=event.width)
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        canvas.bind("<Configure>", on_canvas_configure)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_grid = ttk.Frame(self.scrollable_frame, style="Card.TFrame")
        self.results_grid.pack(fill=tk.X, padx=10)
        
        self.lbl_puntaje = self.create_result_label("📊 Puntaje Calculado", "0.00")
        self.lbl_regla = self.create_result_label("📋 Regla de Decisión", "-")
        self.lbl_prediccion = self.create_result_label("🤖 Predicción del Modelo", "-")
        self.lbl_probabilidad = self.create_result_label("📈 Probabilidad de Éxito", "-")
        
        separator = ttk.Separator(self.scrollable_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=20, padx=10)
        
        ttk.Label(self.scrollable_frame, 
                 text="💡 Explicación Pedagógica",
                 style="Result.TLabel",
                 font=("Segoe UI", 12, "bold")).pack(anchor=tk.W, pady=(0, 10), padx=10)
        
        self.txt_explicacion = tk.Text(self.scrollable_frame, 
                                       height=8, 
                                       wrap=tk.WORD,
                                       bg=COLORS["bg_input"],
                                       fg=COLORS["texto_principal"],
                                       insertbackground=COLORS["texto_principal"],
                                       font=("Segoe UI", 11),
                                       relief=tk.FLAT,
                                       bd=0,
                                       padx=15,
                                       pady=15)
        self.txt_explicacion.pack(fill=tk.BOTH, expand=True, pady=(0, 10), padx=10)
        
        self.resultado_frame.pack_forget()
    
    def create_input_field(self, parent, label_text, attr_name, placeholder):
        container = ttk.Frame(parent, style="Card.TFrame")
        container.pack(fill=tk.X, pady=(0, 15))
        
        label = ttk.Label(container, 
                         text=label_text,
                         style="Result.TLabel",
                         font=("Segoe UI", 11, "bold"))
        label.pack(anchor=tk.W, pady=(0, 8))
        
        entry = StyledEntry(container, style="Styled.TEntry")
        entry.pack(fill=tk.X)
        entry.config(justify="center")
        
        placeholder_label = tk.Label(container,
                                    text=placeholder,
                                    bg=COLORS["bg_input"],
                                    fg=COLORS["texto_secundario"],
                                    font=("Segoe UI", 10),
                                    anchor="w")
        placeholder_label.place(in_=entry, relx=0.02, rely=0.5, anchor="w")
        
        def on_focus_in(event):
            placeholder_label.place_forget()
        
        def on_focus_out(event):
            if not entry.get():
                placeholder_label.place(in_=entry, relx=0.02, rely=0.5, anchor="w")
        
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        
        setattr(self, attr_name, entry)
    
    def create_result_label(self, label_text, default_value):
        container = ttk.Frame(self.results_grid, style="Card.TFrame")
        container.pack(fill=tk.X, pady=8)
        
        label = ttk.Label(container,
                         text=label_text,
                         style="Subheader.TLabel")
        label.pack(anchor=tk.W)
        
        value_label = ttk.Label(container,
                               text=default_value,
                               style="Result.TLabel",
                               font=("Segoe UI", 14, "bold"))
        value_label.pack(anchor=tk.W, pady=(3, 0))
        
        return value_label
    
    def predecir(self):
        try:
            horas = float(self.entry_horas.get())
            asistencia = float(self.entry_asistencia.get())
            tareas = float(self.entry_tareas.get())
            
            if not (1 <= horas <= 20):
                messagebox.showerror("Error de Validación", "Las horas de estudio deben estar entre 1 y 20")
                return
            if not (50 <= asistencia <= 100):
                messagebox.showerror("Error de Validación", "La asistencia debe estar entre 50% y 100%")
                return
            if not (0 <= tareas <= 10):
                messagebox.showerror("Error de Validación", "Las tareas deben estar entre 0 y 10")
                return
            
            puntaje = calcular_puntaje(horas, asistencia, tareas)
            prediccion, probabilidad = predecir(modelo, horas, asistencia, tareas)
            
            self.resultado_frame.pack(fill=tk.BOTH, expand=True)
            
            self.lbl_puntaje.config(text=f"{puntaje:.2f} puntos")
            
            resultado_regla = "✅ APRUEBA" if puntaje >= 12 else "❌ REPRUEBA"
            self.lbl_regla.config(text=resultado_regla,
                                 foreground=COLORS["exito"] if puntaje >= 12 else COLORS["error"])
            
            resultado_modelo = "✅ APRUEBA" if prediccion == 1 else "❌ REPRUEBA"
            self.lbl_prediccion.config(text=resultado_modelo,
                                       foreground=COLORS["exito"] if prediccion == 1 else COLORS["error"])
            
            prob_texto = f"{probabilidad*100:.1f}%"
            self.lbl_probabilidad.config(text=prob_texto,
                                         foreground=COLORS["exito"] if probabilidad >= 0.5 else COLORS["advertencia"])
            
            explicacion = generar_explicacion_ollama(horas, asistencia, tareas, puntaje, probabilidad, prediccion)
            self.txt_explicacion.delete("1.0", tk.END)
            self.txt_explicacion.insert("1.0", explicacion)
            
            self.root.after(100, lambda: self.resultado_frame.pack(fill=tk.BOTH, expand=True))
            
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor ingrese valores numéricos válidos")
    
    def limpiar(self):
        self.entry_horas.delete(0, tk.END)
        self.entry_asistencia.delete(0, tk.END)
        self.entry_tareas.delete(0, tk.END)
        
        self.lbl_puntaje.config(text="0.00")
        self.lbl_regla.config(text="-", foreground=COLORS["texto_principal"])
        self.lbl_prediccion.config(text="-", foreground=COLORS["texto_principal"])
        self.lbl_probabilidad.config(text="-", foreground=COLORS["texto_principal"])
        self.txt_explicacion.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
