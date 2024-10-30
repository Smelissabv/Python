pregunta1 = input(f"¿Como te llamas?")
print(f"Hola {pregunta1}")
while True:
    pregunta2 = input (f"¿Cuál es tu edad?") 
    if int(pregunta2) <= 15:
        print(f"{pregunta1}, te encuentras entrando a tu juventud, aprovecha al máximo el tiempo")
    elif int(pregunta2) >= 16 and int(pregunta2) <=30:
        print(f"{pregunta1}, es una edad donde defines muchas cosas de tu vida")
        break
    else:
        print(f"{pregunta1}, estas en la mejor edad de tu vida")

pregunta3 = input (f"¿Trabajas o estudias?") 
print(f"genial que estes {pregunta3}")
pregunta4 = input (f"En que ciudad vives?") 
print(f"{pregunta4} es un buen lugar para vivir")
pregunta5 = input (f"¿Cuál es tu actividad economica?") 
print(f"{pregunta5} es una buena actividad economica")
numero1 = input("ingrese el valor del numero1: ")
numero2 = input("ingrese el valor del numero2: ")
#El type define si es texto o numero
#EL int toma numeros enteros y el float puede tomar tambien decimales 
numero3 = input("valor 3: ")
numero4 = input("valor4: ")
print((int(numero1) + float(numero2)) * (float(numero3) + float(numero4)))

contador = 0
while contador <= 5:
    print(contador)
    contador +=1

