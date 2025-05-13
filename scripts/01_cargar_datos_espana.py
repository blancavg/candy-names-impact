
import pandas as pd
import os

# Nombres a procesar
nombres = ["susana", "ana", "patricia", "maria"]
ruta_base = "../data/raw/"
salida = []

for nombre in nombres:
    path = os.path.join(ruta_base, f"{nombre}.csv")
    with open(path, encoding='latin-1') as f:
        lines = f.readlines()
    total_line = next(line for line in lines if line.startswith("Total,"))
    valores = total_line.strip().split(",")[6:14]  # 8 décadas
    valores = [int(v.replace(".", "")) if v.replace(".", "").isdigit() else 0 for v in valores]
    salida.append(valores)

decadas = ['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020']
df = pd.DataFrame({'Década': decadas})
for i, nombre in enumerate(nombres):
    df[nombre.upper()] = salida[i]

df.to_csv("../data/processed/frecuencia_espana.csv", index=False)
print("Datos procesados para España guardados.")
