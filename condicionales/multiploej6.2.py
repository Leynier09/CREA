"""
6.2.-múltiplo. Toma dos números N1 y N2 y e indica si N1 es múltiplo de N2.
"""
n1=int(input("Introduce un número: "))
n2=int(input("Introduce otro número: "))

if n2==0:
    print("El segundo número no puede ser igual a 0")

elif n1%n2==0:
    print(n1, "es múltiplo de ", n2)
else: 
    print(n1, "no es múltiplo de ", n2)
    

