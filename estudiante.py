notasMision1 = []
notasMision2 = []
notasMision3 = []
Definitiva = []
estudiantes = []
tamano = int(input("Cuantos estudiantes son: "))
for i in range(tamano):
    estudiante=input("Nombre de estudiante: ")
    estudiantes.append(estudiante)
    notas1=float(input("Nota mision 1: "))
    notasMision1.append(notas1)
    notas2=float(input("Nota mision 2: "))
    notasMision2.append(notas2)
    notas3=float(input("Nota mision 3: "))
    notasMision3.append(notas3)
    promedio = ((float (notas1) + float(notas2) + float(notas3)) / 3)
    Definitiva.append(promedio)
    #no es necesario colocar float en la variable de promedio porque las notas ya lo tienen

i=0

while i<len(estudiantes):
    print(estudiantes[i], Definitiva[i])
    i+=1


   

