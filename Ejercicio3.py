#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en
#cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura>
#es cada una des las asignaturas de la lista y <nota> cada una
#de las correspondientes notas introducidas por el usuario.
Asignaturas = ["Matemáticas", "Física", "Química", "Euskera", "Historia", "Lengua"]
Notas = []
for asignatura in Asignaturas:
    Nota = input("¿Que nota has sacado en " + asignatura + "? ")
    Notas.append(Nota)
for i in range(len(Asignaturas)):
    print("La nota en " + Asignaturas[i] + " es " + Notas[i])