import csv
# with open("datosdechat.csv", "r") as archivo:
#     lector = csv.reader(archivo)
#     for fila in lector:
#         print(fila)

# with open("datosdechat.csv", "r") as archivo:
#     lector = csv.DictReader(archivo)
#     for fila in lector:
#         print(fila)

with open("datosdechat.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["pregunta"], fila ["respuesta"])

