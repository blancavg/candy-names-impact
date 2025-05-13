
import pandas as pd

# Cargar datos procesados
df_esp = pd.read_csv('../data/processed/frecuencia_espana.csv')
df_uru = pd.read_csv('../data/processed/frecuencia_uruguay.csv')

# Guardar tablas consolidadas
df_esp.to_csv('../outputs/tables/frecuencia_absoluta_espana.csv', index=False)
df_uru.to_csv('../outputs/tables/frecuencia_absoluta_uruguay.csv', index=False)

print("Tablas de frecuencia absoluta guardadas.")
