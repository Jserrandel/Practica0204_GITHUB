#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura y elimine de la lista las asignaturas aprobadas. 
#Al final el programa debe mostrar por pantalla las asignaturas
#que el usuario tiene que repetir.
Asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Aprovadas = []
for Asignatura in Asignaturas:
    nota = float(input("¿Qué nota has sacado en " + Asignatura + "? "))
    if nota >= 5:
        Aprovadas.append(Asignatura)
for Asignatura in Aprovadas:
    Asignaturas.remove(Asignatura)
print("Tienes que repetir " + str(Asignaturas))