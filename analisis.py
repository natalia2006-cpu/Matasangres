import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('datos.csv')

# Calcular estadísticas para cada columna
print("=" * 50)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 50)

for columna in df.columns:
    print(f"\nColumna: {columna}")
    print(f"  Media: {df[columna].mean():.2f}")
    print(f"  Mediana: {df[columna].median():.2f}")
    print(f"  Desviación estándar: {df[columna].std():.2f}")

# Generar gráfica de dispersión (scatter plot)
plt.figure(figsize=(10, 6))
plt.scatter(df['col1'], df['col2'], alpha=0.7, s=100, color='blue', edgecolors='black')
plt.xlabel('Columna 1', fontsize=12)
plt.ylabel('Columna 2', fontsize=12)
plt.title('Gráfica de Dispersión: col1 vs col2', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar la gráfica
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
print("\n" + "=" * 50)
print("Gráfica guardada como 'scatter_plot.png'")
print("=" * 50)

# Mostrar la gráfica
plt.show()

