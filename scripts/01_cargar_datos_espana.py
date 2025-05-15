import pandas as pd
from pathlib import Path

# Nombres a procesar y columnas de interés
nombres = ["susana", "maria", "ana", "patricia"]
decadas = ["70s", "80s", "90s", "2000s", "2010s", "2020s"]
ruta_base = "../data/processed/"

# DataFrame base con columna 'decada'
df_final = pd.DataFrame({
    "Década": ["1970", "1980", "1990", "2000", "2010", "2020"]
})

for nombre in nombres:
    path = Path(ruta_base) / f"{nombre}.csv"
    df = pd.read_csv(path)
    print(df)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Sumar cada columna de década, ignorando la primera columna (región)
    sumas = df.iloc[:, 1:].sum()
    df_nombre = pd.DataFrame({
        "Década": ["1970", "1980", "1990", "2000", "2010", "2020"],
        nombre.upper(): sumas.values
    })

    df_final = pd.merge(df_final, df_nombre, on="Década")

# Guardar resultado
output_path = Path("../data/processed/frecuencia_espana.csv")
df_final.to_csv(output_path, index=False)
print(df_final)
print("Resumen nacional por década guardado correctamente.")
