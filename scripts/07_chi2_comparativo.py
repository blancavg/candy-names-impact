
import pandas as pd
from scipy.stats import chi2_contingency

# Cargar datos absolutos de España
df = pd.read_csv('../outputs/tables/frecuencia_absoluta_espana.csv')

# Seleccionar columnas y años relevantes para comparación
cols = ['Década', 'SUSANA', 'PATRICIA']
df_chi = df[cols].copy()
df_chi = df_chi[df_chi['Década'].between(1970, 2010)]  # Filtrado de décadas
df_chi = df_chi.set_index('Década')

# Preparar matriz para chi-cuadrado
chi_data = df_chi.T.values

# Aplicar prueba
stat, p, dof, expected = chi2_contingency(chi_data)

# Mostrar resultados
print("Chi-squared statistic:", round(stat, 2))
print("Degrees of freedom:", dof)
print("p-value:", p)
if p < 0.05:
    print("✅ The difference in decline between 'Susana' and 'Patricia' is statistically significant.")
else:
    print("❌ No statistically significant difference was found.")
