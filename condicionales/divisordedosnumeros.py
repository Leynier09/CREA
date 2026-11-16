""""
Toma dos números N1 y N2 e indica si N1 es divisor de N2.
"""

n1=int(input("Escribe un número: "))
n2=int(input("Escribe otro número: "))
if n2%n1==0:
    print("El número ", n1, "es divisor de ", n2)
else:
    print("El número ", n1, "no es divisor de ", n2)



