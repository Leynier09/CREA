"""
Realiza un programa en pyhton que tome números de entrada hasta que le des 0. A continuación debe mostrar el número de pares, impares, positivos y negativos. El 0 no cuenta.

Ej. Si le damos: 2, 3, 5, -3 , -2, 8, 10 -6, -1, 34, 0
"""
n=1
while n!=0:
    n=int(input("Introduce un número"))
if n==0:

    if n>0:
        print (n, " es positivo")
    else:
        print(n, " es negativo")