# Este programa lee un archivo Excel que contiene las calificaciones de varios alumnos.
# Luego, agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100, y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Leer el archivo Excel y cargar los datos en un DataFrame de pandas
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Generar valores aleatorios entre 0 y 100 con un decimal para la nueva columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, len(df)), 1)

# Guardar el DataFrame actualizado de vuelta en el archivo Excel
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)
