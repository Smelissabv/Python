lista = [1,2,3,4,5,6,7,8,9]
i=0
#print(len(lista))
lista.append(11)
while i<len(lista):
    print(lista[i])
    i+=1

lista = []
tamano = int(input("ingrese el tamaño de la lista: "))
while tamano != 0:
    valor=input("ingrese el elemento de la lista: ")
    lista.append(valor)
    tamano -=1
i=0

lista = []
tamano = int(input("ingrese el tamaño de la lista: "))
for i in range(tamano):
    valor=input("ingrese el elemento de la lista: ")
    lista.append(valor)
print(lista)

lista = ["¿Como te llamas?", "¿Cuál es tu edad?","¿Trabajas o estudias?"]
respuestas = []
for i in range(len(lista)):
    print({lista[i]})
    respuesta = input()
    respuestas.append(respuesta)
print(respuestas)






