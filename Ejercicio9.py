#Escribir un programa que pida al usuario una palabra
#y muestre por pantalla el número de veces que contiene cada vocal.
Palabra = input("Introduce una palabra: ").lower()
Vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in Vocales: 
    Tiempo = 0
    for Letra in Palabra: 
        if Letra == vocal:
            Tiempo += 1
    print("La vocal " + vocal + " aparece " + str(Tiempo) + " veces")