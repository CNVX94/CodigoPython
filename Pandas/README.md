# Pandas y CSV - Tutorial Práctico

Este proyecto contiene un tutorial completo sobre el uso de la biblioteca Pandas en Python para trabajar con archivos CSV.

## Descripción

El archivo `pandasycsv.py` es un tutorial paso a paso que cubre las operaciones fundamentales de análisis de datos con Pandas. Este material fue originalmente desarrollado en Google Colab y ha sido adaptado para uso local.

## Contenido del Tutorial

### 1. Carga de Datos
- Importación de archivos CSV utilizando pandas
- Lectura y visualización inicial de datos
- Uso del método `read_csv()`

### 2. Exploración Básica
- Visualización de las primeras y últimas filas (`head()`, `tail()`)
- Información técnica del DataFrame (`info()`)
- Resumen estadístico de los datos (`describe()`)
- Exploración de nombres de columnas

### 3. Limpieza de Datos
- Identificación de valores nulos/faltantes (NaN)
- Conteo y porcentaje de valores nulos
- Eliminación de filas con valores faltantes (`dropna()`)
- Relleno de valores faltantes con ceros (`fillna()`)
- Eliminación de columnas innecesarias

**Conceptos clave:**
- ¿Qué es un valor nulo?: Un espacio vacío en el dataset que no tiene información, representado como `NaN` o `None`
- Causas: Errores de captura, datos no disponibles, campos opcionales
- Impacto: Pueden afectar cálculos y análisis

### 4. Filtrado y Selección de Datos
- Filtrado de filas con condiciones simples
- Filtrado con múltiples condiciones usando operadores lógicos:
  - `&` (AND): Ambas condiciones deben cumplirse
  - `|` (OR): Al menos una condición debe cumplirse
  - `~` (NOT): Negación de una condición
- Selección de rangos específicos (ejemplo: edades entre 18 y 50 años)

### 5. Operaciones y Agrupación
- Cálculos estadísticos: suma (`sum()`), media (`mean()`)
- Agrupación de datos por columnas (`groupby()`)
- Cálculo de estadísticas por grupos
- Creación de tablas pivote (`pivot_table()`)

### 6. Manipulación de Datos
- Ordenamiento de DataFrames (`sort_values()`)
- Transformación y reorganización de datos

### 7. Guardar Resultados
- Exportación de DataFrames modificados a CSV
- Uso del método `to_csv()`

## Requisitos

```bash
pip install pandas
```

## Uso

El script trabaja con un archivo CSV llamado `mv.csv`. Para ejecutar el tutorial:

1. Asegúrate de tener el archivo CSV en la ruta especificada
2. Ejecuta el script:
   ```bash
   python pandasycsv.py
   ```

## Notas Importantes

- El código original fue diseñado para Google Colab, por lo que algunas rutas de archivo pueden necesitar ajuste para ejecución local
- La ruta del CSV en el código es: `/content/CSV/mv.csv` - modifícala según tu estructura de carpetas
- Algunas operaciones modifican el DataFrame original, lo que puede afectar el código subsecuente

## Estructura de Datos

El dataset `mv.csv` contiene las siguientes columnas:
- `edad`: Edad de los participantes
- `sexo`: Género
- `time`: Tiempo
- `carrera`: Información sobre carrera/programa
- `acepta`: Variable de aceptación
- `trabajo`: Estado laboral

## Objetivo Educativo

Este tutorial está diseñado para:
- Aprender operaciones básicas e intermedias con Pandas
- Comprender el flujo de trabajo de análisis de datos
- Practicar limpieza y transformación de datos
- Dominar filtrado y agrupación de información
- Exportar resultados procesados

---

**Nota:** Este es un material educativo para practicar análisis de datos con Python y Pandas.
