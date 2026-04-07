Actividad: Predicción de aprobación de estudiantes
El usuario captura:
•	Horas de estudio por semana (1 a 20 horas)
•	Porcentaje de asistencia (50% a 100%)
•	Número de tareas entregadas (0 a 10 tareas)
Incluir esta regla como puntaje: 
Puntaje= (0.35*horas de estudio+0.08 *asistencia+0.6*tareas entregadas)
Si el puntaje es >= 12 aprueba
El sistema:
•	Usa el modelo de regresión logística, entrenado con datos simulados, predice si el alumno aprueba o no, muestra la probabilidad y Gemini genera una explicación pedagógica del resultado.
Hacer la interfaz gráfica en Tkinter
Nota: La variable X= incluye horas de estudio, asistencia y tareas entregadas. La variable Y= solo tiene aprueba o no.
