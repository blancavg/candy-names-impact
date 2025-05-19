
import pandas as pd

def calcular_frecuencia_relativa(df, nombres):
    df = df.copy()
    df['TOTAL'] = df[nombres].sum(axis=1)
    for nombre in nombres:
        df[nombre] = df[nombre] / df['TOTAL']
    return df[['Década'] + nombres]

# Cargar datos absolutos
df_esp = pd.read_csv('../outputs/tables/frecuencia_absoluta_espana.csv')
df_uru = pd.read_csv('../outputs/tables/frecuencia_absoluta_uruguay.csv')
nombres = ['SUSANA', 'ANA', 'PATRICIA', 'MARIA']

# Calcular frecuencia relativa
df_esp_rel = calcular_frecuencia_relativa(df_esp, nombres)
df_uru_rel = calcular_frecuencia_relativa(df_uru, nombres)

# Guardar tablas
df_esp_rel.to_csv('../outputs/tables/frecuencia_relativa_espana.csv', index=False)
df_uru_rel.to_csv('../outputs/tables/frecuencia_relativa_uruguay.csv', index=False)

print("Tablas de frecuencia relativa guardadas.")
