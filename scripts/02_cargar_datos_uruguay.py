
import pandas as pd

# Cargar dataset completo
df = pd.read_csv('../data/raw/nombre_nacim_x_anio_sexo.csv')

# Filtrar por nombres y sexo femenino
nombres_objetivo = ['SUSANA', 'ANA', 'PATRICIA', 'MARIA']
df = df[df['SEXO'] == 'F']
df = df[df['NOMBRE'].isin(nombres_objetivo)]

# Crear columna de década
df['decada'] = (df['ANIO'] // 10) * 10

# Agrupar por década y nombre
df_decada = df[df['ANIO'].between(1970, 2019)]
df_resumen = df_decada.groupby(['decada', 'NOMBRE'])['NACIMIENTOS'].sum().reset_index()

# Pivotear tabla
df_pivot = df_resumen.pivot(index='decada', columns='NOMBRE', values='NACIMIENTOS').fillna(0).astype(int).reset_index()
df_pivot.columns.name = None
df_pivot.rename(columns={'decada': 'Década'}, inplace=True)

# Guardar
df_pivot.to_csv('../data/processed/frecuencia_uruguay.csv', index=False)
print("Datos procesados para Uruguay guardados.")
