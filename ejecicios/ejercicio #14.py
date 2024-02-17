# Escribir una función que calcule la media
# aritmética de una lista de números.

def media_aritmetica(lista):
    suma= 0
    for numero in lista:
        suma += numero

    promedio = suma / len(lista)
    return promedio


lista= [1,2,3,4,5]
print(media_aritmetica(lista))
