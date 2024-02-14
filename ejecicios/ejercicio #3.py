#Crear un programa que genere una lista de números
#aleatorios y los imprima en pantalla

import random


def generar_numeros_aleatorios(cantidad, rango_inferior, rango_superior):
    numeros_aleatorios = [random.randint(rango_inferior, rango_superior) for _ in range(cantidad)]
    return numeros_aleatorios

#ejemplo
cantidad = 10
rango_inferior = 1
rango_superior = 100
numeros_aleatorios = generar_numeros_aleatorios(cantidad, rango_inferior, rango_superior)
print(f"La lista de {cantidad} números aleatorios entre {rango_inferior} y"
      f" {rango_superior} es: {numeros_aleatorios}")
