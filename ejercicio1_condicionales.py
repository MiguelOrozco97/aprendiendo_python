"""
Estructuras de Control - Condicionales
Escribe un programa en Python que solicite al usuario ingresar un número. Luego, el programa debe imprimir si ese número es par o impar.
"""

num = int(input("Ingresa un numero: "))
residuo = num % 2;
if (residuo ==0):
    print("El numero es par")
elif residuo != 0:
    print("El numero es impar")