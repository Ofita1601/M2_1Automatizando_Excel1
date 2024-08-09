# Este programa lee un archivo Excel que contiene las calificaciones de varios alumnos en diferentes materias.
# Luego, grafica las calificaciones para cada alumno, asegurando que las etiquetas de los alumnos en el eje X no se encimen.

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo Excel y cargar los datos en un DataFrame de pandas
df = pd.read_excel('calificaciones_alumnos.xlsx')

# Crear una figura y un conjunto de subgráficos para manejar los gráficos
plt.figure(figsize=(10, 6))

# Para cada alumno, graficar sus calificaciones
for i, row in df.iterrows():
    plt.plot(['Cálculo Integral', 'Programación OOP', 'Estructura de Datos'],
             [row['Mat_CalculoIntegral'], row['Mat_ProgramacionOOP'], row['Mat_EstructuraDatos']],
             marker='o', label=row['Nombre'])

# Agregar un título al gráfico
plt.title('Calificaciones de los Alumnos por Materia')

# Rotar las etiquetas del eje X para que no se encimen
plt.xticks(rotation=45)

# Agregar etiquetas a los ejes
plt.xlabel('Materias')
plt.ylabel('Calificaciones')

# Agregar una leyenda con los nombres de los alumnos
plt.legend(title="Alumnos", bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar el gráfico para que se vea mejor
plt.tight_layout()

# Mostrar el gráfico
plt.show()
