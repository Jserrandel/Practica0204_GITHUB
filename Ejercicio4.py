#Escribir un programa que pregunte al usuario los números ganadores de la 
#lotería primitiva, los almacene en una lista y los muestre por
#pantalla ordenados de menor a mayor.
Premio = []
for i in range(6):
    Premio.append(int(input("Introduce un número ganador: ")))
Premio.sort()
print("Los números ganadores son " + str(Premio))