import pandas as pd
acumulador = 0
lista = [1, 2, 3, 4, 5]
#Crear una serie
for element in lista:
    acumulador += element
print(acumulador/len(lista))

mi_serie = pd.Series(lista)
promedio = mi_serie.mean()
print(promedio)

#dataFrame