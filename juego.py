import random
intentos=0
numero = random.randint(1,100)
while True:
    intentos+=1
    print("ingrese un numero: ")
    comparar = int(input())
    if comparar == numero:
        print("has ganado")
        break
    elif comparar < numero:
        print("el numero es mayor")
    else:
        print("el numero es menor")