"""
Listas y Bucles - Ciclo For
Escribe un programa en Python que solicite al usuario ingresar una lista de números separados por espacios. Luego, el programa debe imprimir la suma de todos los números en la lista.

Aquí tienes una guía para hacerlo:

Utiliza la función input() para solicitar al usuario que ingrese una lista de números separados por espacios.
Utiliza el método split() para separar los números ingresados por el usuario en una lista.
Utiliza un bucle for para iterar sobre cada número en la lista.
Convierte cada número a un entero utilizando la función int().
Suma todos los números y almacena el resultado en una variable.
Imprime la suma de todos los números.
"""

num = input("Ingrese 4 numeros separados: ")
lista_num = num.split()
suma = 0

for x in lista_num:
    suma += int(x)
print("La suma de todos los numeros es: ", suma)