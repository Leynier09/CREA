par=0
impar=0
for i in range(1, 11):
    n=int(input("Ingrese un número: "))
    if n%2==0:
        par=par+1
    else:
        impar=impar+1
    print("hay", par, "números pares y ", impar, "números impares")
