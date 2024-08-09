# Este programa lee un archivo Excel que contiene calificaciones de varios alumnos
# y muestra el número de registros (filas) y el número de campos (columnas) en la tabla.

import pandas as pd

# Leer el archivo Excel y cargar los datos en un DataFrame de pandas
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Obtener el número de registros (filas) en el DataFrame
num_registros = len(df)

# Obtener el número de campos (columnas) en el DataFrame
num_campos = len(df.columns)

# Imprimir el número de registros y campos
print(f'Número de registros (filas): {num_registros}')
print(f'Número de campos (columnas): {num_campos}')