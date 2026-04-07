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
        else:
            resultado = "ESTABLE - Cliente probablemente no abandonará"
            nivel_riesgo = "Bajo"

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

        texto_resultado.config(state='normal')
        texto_resultado.delete('1.0', tk.END)
        texto_resultado.insert('1.0', f"Resultado: {resultado}\n\nProbabilidad de abandono: {probabilidad:.1%}\n\n--- Análisis de Ollama ---\n\n{ollama_resp}")
        texto_resultado.config(state='disabled')

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos en todos los campos")

root = tk.Tk()
root.title("Predicción de Abandono de Clientes")
root.geometry("600x700")
root.configure(bg='#f0f0f0')

tk.Label(root, text="Predicción de Churn de Clientes", font=('Arial', 16, 'bold'), bg='#f0f0f0').pack(pady=10)

frame_inputs = ttk.LabelFrame(root, text="Datos del Cliente")
frame_inputs.pack(padx=20, pady=10, fill='x')

tk.Label(frame_inputs, text="Meses de antigüedad:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_antiguedad = ttk.Entry(frame_inputs)
entry_antiguedad.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Pago mensual ($):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_pago = ttk.Entry(frame_inputs)
entry_pago.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Número de quejas:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_quejas = ttk.Entry(frame_inputs)
entry_quejas.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Horas de uso por semana:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_uso = ttk.Entry(frame_inputs)
entry_uso.grid(row=3, column=1, padx=10, pady=5)

ttk.Button(root, text="Predecir Abandono", command=predecir).pack(pady=10)

frame_resultado = ttk.LabelFrame(root, text="Resultado")
frame_resultado.pack(padx=20, pady=10, fill='both', expand=True)

texto_resultado = tk.Text(frame_resultado, height=15, wrap='word')
texto_resultado.pack(padx=10, pady=10, fill='both', expand=True)
texto_resultado.config(state='disabled')

root.mainloop()