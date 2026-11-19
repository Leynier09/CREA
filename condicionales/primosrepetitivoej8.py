#Modifica el ejercicio anterior de manera que te pida números, te diga si es primo y termine cuando le des un cero.

while x!=0:
    x=int(input("Introduce un número: "))
    if x%2==0:
        print("El número es primo")