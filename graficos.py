# #instalar cualquier libreria que vayamos a usar:

import matplotlib.pyplot as plt

# # datos de ejemplo grafico de barras

# categorias = ["A", "B", "C", "D"]
# valores = [10, 15, 7, 10]

# #crear grafico de barras
# plt.bar(categorias, valores, color="skyblue")
# plt.title("grafico de barras")
# plt.xlabel("categorias")
# plt.ylabel("valores")
# plt.show()

#grafico de lineas
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.plot(x, y, marker="o", color="green", linestyle="-")
# plt.title("Grafico de lineas")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.show()

#grafico de dispersion
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# # Crear gráfico de dispersión
# plt.scatter(x, y, color="purple", linestyle="-")
# plt.title("Gráfico de Dispersión")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.show()

# #Histograma
# # Datos de ejemplo
# datos = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]

# # Crear histograma
# plt.hist(datos, bins=5, color="orange", edgecolor="black")
# plt.title("Histograma")
# plt.xlabel("Valores")
# plt.ylabel("Frecuencia")
# plt.show()

# #Mapas de calor
# import numpy as np

# datos = np.random.rand(10, 10)
# # Crear mapa de calor
# plt.imshow(datos, cmap="viridis", interpolation="nearest")
# plt.title("Mapa de Calor")
# plt.colorbar()
# plt.show()
           
# #Grafico circular
# Datos de ejemplo
categorias = ["Categoría A", "Categoría B", "Categoría C"]
tamaños = [40, 35, 25]

# Crear gráfico circular
plt.pie(tamaños, labels=categorias, autopct="%1.1f%%", startangle=140)
plt.title("Gráfico Circular")
plt.show()