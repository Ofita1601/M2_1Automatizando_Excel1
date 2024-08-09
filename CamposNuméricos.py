# Este programa lee un archivo Excel que contiene calificaciones de varios alumnos
# y muestra qué campos (columnas) son numéricos.

import pandas as pd

# Leer el archivo Excel y cargar los datos en un DataFrame de pandas
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Identificar columnas numéricas
# Utiliza el método select_dtypes para seleccionar solo las columnas con tipos de datos numéricos
columnas_numericas = df.select_dtypes(include='number').columns

# Imprimir los nombres de las columnas numéricas
print('Campos numéricos:')
for columna in columnas_numericas:
    print(columna)