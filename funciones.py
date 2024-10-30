def saludar():
    print("hola mundo")
saludar()

def saludar(nombre):
    print(f"hola {nombre}!")
saludar("Ana")

def multiplicar(a, b):
    return a * b
resultado = multiplicar(5, 3)
print(resultado)

def sumar(c, d):
    return c + d
numero1=input("ingresar numero 1: ")
numero2=input("ingresar numero 2: ")
resultado = sumar(numero1, numero2)
print(resultado)

suma = lambda x, y: x + y
resultado = suma(4, 7)
print(resultado)