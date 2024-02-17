#Crear un programa que pida al usuario ingresar
# dos números y calcule su suma, resta, multiplicación y división.


n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
if n2 !=0:
    division = n1 // n2
else:
    print("Error no se puede dividir por 0")

print(f"La suma de {n1} y {n2} es: {suma}")
print(f"La resta de {n1} y {n2} es: {resta}")
print(f"La multiplicación de {n1} y {n2} es: {multiplicacion}")
print(f"La división de {n1} y {n2} es: {division}")




