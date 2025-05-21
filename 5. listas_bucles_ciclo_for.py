"""
Listas y Bucles - Ciclo For
Escribe un programa en Python que solicite al usuario ingresar una lista de números separados por espacios. Luego, el programa debe imprimir la suma de todos los números en la lista.


* la función input() se usa para solicitar al usuario que ingrese datos.
* el método split() se usa para separar los números ingresados por el usuario en una lista.
* se usa un bucle for para iterar sobre cada número en la lista.
* la función int() se usa para convertir datos a numeros enteros.
"""

num = input("Ingrese 4 numeros separados: ")
lista_num = num.split()
suma = 0

for x in lista_num:
    suma += int(x)
print("La suma de todos los numeros es: ", suma)