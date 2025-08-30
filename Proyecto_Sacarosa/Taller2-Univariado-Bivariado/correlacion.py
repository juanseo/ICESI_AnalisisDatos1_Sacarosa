import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("DatosAreaMolinosRed.csv", sep=";")

# Convertir columna de tiempo a datetime
data['Time'] = pd.to_datetime(data['Time'])

# Poner fecha como índice
data = data.set_index('Time')

# Reagrupar por intervalos de 10 minutos y sacar promedio
df_resample = data.resample('3H').mean()



# 3. Calcular la matriz de correlación (Pearson por defecto)
correlation_matrix = df_resample.corr(method='pearson')

# 4. Mostrar la matriz en consola
print("\nMatriz de correlación:")
print(correlation_matrix)

# 5. Visualizar la correlación como mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlación")
plt.show()