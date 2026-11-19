#Toma un número y comprueba si es primo o no.

x=int(input("Introduce un número: "))
n=0
for i in range (1, x+1):
    if x%i==0:
            n=n+1
if n==2 or n==1:
    print("El número ", x, "es primo")
else:
    print("El número ", x, " no es primo")

