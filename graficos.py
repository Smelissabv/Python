#instalar cualquier libreria que vayamos a usar:

import matplotlib.pyplot as plt

# datos de ejemplo

categorias = ["A", "B", "C", "D"]
valores = [10, 15, 7, 10]

#crear grafico de barras
plt.bar(categorias, valores, color="skyblue")
plt.title("grafico de barras")
plt.xlabel("categorias")
plt.ylabel("valores")
plt.show()
