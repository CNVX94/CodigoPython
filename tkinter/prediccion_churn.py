import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import ollama
import numpy as np

OLLAMA_MODEL = "deepseek-v3.1:671b-cloud"

X_train = np.array([
    [24, 49.99, 0, 20],
    [6, 29.99, 2, 5],
    [36, 79.99, 0, 35],
    [12, 39.99, 3, 8],
    [48, 89.99, 1, 40],
    [3, 19.99, 1, 3],
    [18, 59.99, 0, 25],
    [30, 69.99, 2, 15],
    [8, 34.99, 4, 6],
    [42, 84.99, 0, 38],
    [15, 44.99, 1, 12],
    [21, 54.99, 0, 22],
    [9, 29.99, 3, 7],
    [45, 94.99, 1, 42],
    [5, 24.99, 2, 4],
])
y_train = np.array([0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
model = LogisticRegression()
model.fit(X_scaled, y_train)


def predecir():
    try:
        antiguedad = float(entry_antiguedad.get())
        pago = float(entry_pago.get())
        quejas = int(entry_quejas.get())
        uso = float(entry_uso.get())

        X_new = scaler.transform([[antiguedad, pago, quejas, uso]])
        prediccion = model.predict(X_new)[0]
        probabilidad = model.predict_proba(X_new)[0][1]

        if prediccion == 1:
            resultado = "ALTO RIESGO - Cliente en riesgo de abandono"
            nivel_riesgo = "Alto"
            color_riesgo = "#e74c3c"
        else:
            resultado = "ESTABLE - Cliente probablemente no abandonará"
            nivel_riesgo = "Bajo"
            color_riesgo = "#27ae60"

        prompt = f"""Eres un analista de retención de clientes. Con los siguientes datos de un cliente:
- Antigüedad: {antiguedad} meses
- Pago mensual: ${pago}
- Quejas: {quejas}
- Uso semanal: {uso} horas
- Predicción del modelo: {resultado}
- Probabilidad de abandono: {probabilidad:.1%}

Genera una respuesta breve (máx 3 párrafos) con:
1. Explicación breve del resultado
2. Nivel de riesgo (Alto/Medio/Bajo)
3. Una recomendación de retención específica
4. Acción sugerida para el área comercial"""

        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        ollama_resp = response["message"]["content"]

        label_resultado.config(
            text=f"Resultado: {resultado}",
            foreground=color_riesgo
        )
        label_probabilidad.config(text=f"Probabilidad de abandono: {probabilidad:.1%}")
        
        texto_resultado.config(state='normal')
        texto_resultado.delete('1.0', tk.END)
        texto_resultado.insert('1.0', f"--- Análisis de Ollama ---\n\n{ollama_resp}")
        texto_resultado.config(state='disabled')
        
        frame_resultado.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        root.update_idletasks()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos en todos los campos")


def on_resize(event):
    width = event.width
    if width < 500:
        frame_inputs.columnconfigure(0, weight=0)
        frame_inputs.columnconfigure(1, weight=1)
    else:
        frame_inputs.columnconfigure(0, weight=1)
        frame_inputs.columnconfigure(1, weight=2)


root = tk.Tk()
root.title("Predicción de Abandono de Clientes")
root.geometry("700x750")
root.minsize(500, 650)
root.configure(bg='#f5f6fa')

style = ttk.Style()
style.theme_use('clam')
style.configure('Title.TLabel', font=('Segoe UI', 20, 'bold'), background='#f5f6fa', foreground='#2c3e50')
style.configure('Card.TLabelframe', background='#ffffff', borderwidth=2, relief='flat')
style.configure('Card.TLabelframe.Label', font=('Segoe UI', 12, 'bold'), background='#ffffff', foreground='#2c3e50')
style.configure('TLabel', font=('Segoe UI', 10), background='#ffffff', foreground='#34495e')
style.configure('TEntry', font=('Segoe UI', 10))
style.configure('Primary.TButton', font=('Segoe UI', 11, 'bold'))
style.map('Primary.TButton', background=[('active', '#3498db')])

header_frame = tk.Frame(root, bg='#2c3e50', height=80)
header_frame.pack(fill='x')
header_frame.pack_propagate(False)

tk.Label(
    header_frame,
    text="Predicción de Churn de Clientes",
    font=('Segoe UI', 18, 'bold'),
    bg='#2c3e50',
    fg='white'
    
).pack(pady=20)

tk.Label(
    header_frame,
    text="Sistema de análisis predictivo para retención",
    font=('Segoe UI', 10),
    bg='#2c3e50',
    fg='#bdc3c7'
).pack(pady=5)


main_frame = tk.Frame(root, bg='#f5f6fa')
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

info_frame = tk.Frame(main_frame, bg='#f5f6fa')
info_frame.pack(fill='x', pady=(0, 15))

info_text = tk.Label(
    info_frame,
    text="💡 Ingrese los datos del cliente para predecir la probabilidad de abandono",
    font=('Segoe UI', 10),
    bg='#f5f6fa',
    fg='#7f8c8d'
)
info_text.pack()

frame_inputs = ttk.LabelFrame(main_frame, text="Datos del Cliente", style='Card.TLabelframe', padding=20)
frame_inputs.pack(fill='x', pady=10)

frame_inputs.columnconfigure(0, weight=1)
frame_inputs.columnconfigure(1, weight=2)

labels = [
    ("Meses de antigüedad:", "entry_antiguedad", "24"),
    ("Pago mensual ($):", "entry_pago", "49.99"),
    ("Número de quejas:", "entry_quejas", "0"),
    ("Horas de uso por semana:", "entry_uso", "20")
]

entries = {}

for i, (label_text, var_name, default) in enumerate(labels):
    label = ttk.Label(frame_inputs, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=12, sticky='e')
    
    entry = ttk.Entry(frame_inputs, font=('Segoe UI', 11))
    entry.insert(0, default)
    entry.grid(row=i, column=1, padx=10, pady=12, sticky='ew')
    entries[var_name] = entry

entry_antiguedad = entries['entry_antiguedad']
entry_pago = entries['entry_pago']
entry_quejas = entries['entry_quejas']
entry_uso = entries['entry_uso']

button_frame = tk.Frame(main_frame, bg='#f5f6fa')
button_frame.pack(fill='x', pady=15)

btn_predecir = tk.Button(
    button_frame,
    text="🔮 Predecir Abandono",
    command=predecir,
    font=('Segoe UI', 12, 'bold'),
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    activeforeground='white',
    relief='flat',
    cursor='hand2',
    padx=25,
    pady=10
)
btn_predecir.pack()

frame_resultado = ttk.LabelFrame(main_frame, text="Resultado del Análisis", style='Card.TLabelframe', padding=15)

resultado_header = tk.Frame(frame_resultado, bg='#ffffff')
resultado_header.pack(fill='x', pady=(0, 10))

label_resultado = tk.Label(
    resultado_header,
    text="Esperando predicción...",
    font=('Segoe UI', 14, 'bold'),
    bg='#ffffff',
    fg='#7f8c8d'
)
label_resultado.pack(anchor='w')

label_probabilidad = tk.Label(
    resultado_header,
    text="",
    font=('Segoe UI', 11),
    bg='#ffffff',
    fg='#34495e'
)
label_probabilidad.pack(anchor='w')

separator = ttk.Separator(frame_resultado, orient='horizontal')
separator.pack(fill='x', pady=10)

texto_resultado = tk.Text(
    frame_resultado,
    height=12,
    wrap='word',
    font=('Segoe UI', 10),
    bg='#fafafa',
    fg='#2c3e50',
    relief='flat',
    borderwidth=1
)
texto_resultado.pack(fill='both', expand=True)
texto_resultado.config(state='disabled')

scrollbar = ttk.Scrollbar(frame_resultado, command=texto_resultado.yview)
texto_resultado.configure(yscrollcommand=scrollbar.set)

footer_frame = tk.Frame(root, bg='#ecf0f1', height=40)
footer_frame.pack(fill='x')
footer_frame.pack_propagate(False)

tk.Label(
    footer_frame,
    text="© 2026 Sistema de Predicción de Churn | Powered by ML + Ollama",
    font=('Segoe UI', 8),
    bg='#ecf0f1',
    fg='#7f8c8d'
).pack(pady=10)

root.bind('<Configure>', on_resize)

root.mainloop()
