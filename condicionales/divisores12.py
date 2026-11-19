""""
 Toma un número de entrada y visualiza el número de divisores que tiene. Ej si le das el 12 debe devolver: el 12 tiene 6 divisores.
"""
x=int(input("Introduce un número: "))
n=0
for i in range (1, x+1):
    if x%i==0:
            n=n+1
print("El número ", x, " tiene ", n, " divisores")