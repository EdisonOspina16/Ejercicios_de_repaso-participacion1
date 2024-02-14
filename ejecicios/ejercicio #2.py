#Escribir una función que calcule el área de un círculo dado su radio
import math


def area_circulo(radio):
    if radio >=0:
        area = math.pi * radio ** 2
        return area
    else:
        return None