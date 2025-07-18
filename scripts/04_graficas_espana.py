
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df_abs = pd.read_csv('../outputs/tables/frecuencia_absoluta_espana.csv')
df_rel = pd.read_csv('../outputs/tables/frecuencia_relativa_espana.csv')

# Paleta de colores
palette = {'SUSANA': '#D62728', 'ANA': '#1F77B4', 'PATRICIA': '#2CA02C', 'MARIA': '#9467BD'}

# Frecuencia absoluta
df_abs_plot = df_abs.melt(id_vars='Década', var_name='Nombre', value_name='Frecuencia')
plt.figure(figsize=(10,6))
sns.lineplot(data=df_abs_plot, x='Década', y='Frecuencia', hue='Nombre', palette=palette, marker="o")
plt.title("Frecuencia absoluta de nombres en España")
plt.grid(True)
plt.tight_layout()
plt.savefig('../outputs/plots/frecuencia_absoluta_espana.png')
plt.close()

# Frecuencia relativa
df_rel_plot = df_rel.melt(id_vars='Década', var_name='Name', value_name='Relative frequency')
plt.figure(figsize=(10,6))
sns.lineplot(data=df_rel_plot, x='Década', y='Relative frequency', hue='Name', palette=palette,
             marker="o", markersize= 12, linewidth=2)
plt.title("Susana's trend - Spain")
plt.xlabel("Decade", fontsize=14)
plt.ylabel("Relative frequency", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.grid(True)
plt.tight_layout()
plt.savefig('../outputs/plots/frecuencia_relativa_espana.png')
plt.close()

print("Gráficas de España guardadas.")
