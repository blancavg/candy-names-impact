
import pandas as pd

def to_markdown_table(df, title):
    print(f"\n### {title}\n")
    print(df.to_markdown(index=False))

# Cargar tablas
df_abs_esp = pd.read_csv('../outputs/tables/frecuencia_absoluta_espana.csv')
df_rel_esp = pd.read_csv('../outputs/tables/frecuencia_relativa_espana.csv')
df_abs_uru = pd.read_csv('../outputs/tables/frecuencia_absoluta_uruguay.csv')
df_rel_uru = pd.read_csv('../outputs/tables/frecuencia_relativa_uruguay.csv')

# Generar markdown para cada tabla
to_markdown_table(df_abs_esp, "Frecuencia Absoluta - España")
to_markdown_table(df_rel_esp, "Frecuencia Relativa - España")
to_markdown_table(df_abs_uru, "Frecuencia Absoluta - Uruguay")
to_markdown_table(df_rel_uru, "Frecuencia Relativa - Uruguay")
