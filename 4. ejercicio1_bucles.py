"""
Bucles - Ciclo While
Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. Luego, el programa debe imprimir todos los números desde 1 hasta el número ingresado por el usuario, utilizando un bucle while.
"""

num = int(input("Ingrese un numero: "))
contador = 1

while contador <= num:
    print(contador)
    contador+=1