#Escribir un programa que almacene en una lista los siguientes precios,
#50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor 
#de los precios.
Precios = [50, 75, 46, 22, 80, 65, 8]
min = max = Precios[0]
for precio in Precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))