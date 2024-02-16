#Crear un programa que genere una lista de números pares entre 1 y 100

numeros_pares = []

for numero in range(1, 101):
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(numeros_pares)