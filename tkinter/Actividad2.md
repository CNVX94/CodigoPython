# Predicción de abandono de clientes (churn) con Regresión Logística + Gemini + Tkinter
Api= AIzaSyAerAziDkk3ynUxwOHIuIFILPiqka0drmU

Este proyecto predice si un cliente de un servicio digital podría **cancelar su suscripción** con base en variables simples, y luego Gemini genera una **explicación comercial** y una **recomendación de retención** en lenguaje natural. La forma actual recomendada por Google para Python usa `from google import genai, genai.Client()` y `client.models.generate_content(...)` con el SDK oficial Google GenAI.

## Qué hace la app

La interfaz pide estos datos del cliente:

- meses de antigüedad
- pago mensual
- número de quejas
- uso del servicio en horas por semana

El modelo de **regresión logística** predice:

- \( 0 = \text{cliente estable} \)
- \( 1 = \text{cliente en riesgo de abandono} \)

Después, Gemini redacta algo como:

- explicación del resultado
- nivel de riesgo
- recomendación para retener al cliente
- acción sugerida para el área comercial

**Por qué este ejemplo sí sirve**

Porque combina tres cosas muy claras:

- **Machine Learning clásico** con scikit-learn
- **Interfaz gráfica** con Tkinter
- **IA generativa** con Gemini para explicar resultados

Además, es un caso muy común en negocios, marketing y analítica de clientes.