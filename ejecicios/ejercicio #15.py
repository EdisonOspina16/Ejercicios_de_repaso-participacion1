#Crear un programa que pida al usuario ingresar una
# cadena de texto y determine si es un palíndromo o no.


cadena = input("Ingrese una cadena de texto: ")
cadena = cadena.lower().replace(" ", "")

inversa = cadena[::-1]

if cadena == inversa:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")
