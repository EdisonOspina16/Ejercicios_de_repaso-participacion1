#Crear un programa que calcule la suma de los números en una lista dada.


def suma_de_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

lista = [1, 2, 3, 4, 5]
print(suma_de_lista(lista))


