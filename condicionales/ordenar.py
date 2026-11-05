
n1=int(input("Introduce un número: "))
n2=int(input("Introduce otro número: "))
n3=int(input("Introduce otro número: "))

if n1<n2:
    if n1<n3:
        if n2<n3:
            print("De menor a mayor es: ", n1, n2, n3)
        else:
            print("De menor a mayor es: ", n1, n3, n2)

if n2<n1:
    if n2<n3:
        if n3<n1:
            print("De menor a mayor es: ", n2, n3, n1)
        else: 
            print("De menor a mayor es: ", n2, n1, n3)

if n3<n1:
    if n3<n2:
        if n1<n2:
            print("De menor a mayor es: ", n3, n1, n2)

        else: 
            print("De menor a mayor es: ", n3, n2, n1)