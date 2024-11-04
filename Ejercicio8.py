#Escribir un programa que pida al usuario una
#palabra y muestre por pantalla si es un palíndromo.
Letra = input("Introduce una palabra: ")
Letra_Reves = Letra
Letra = list(Letra)
Letra_Reves = list(Letra_Reves)
Letra_Reves.reverse()
if Letra == Letra_Reves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")