x=int(input("Ingrese un número: "))
y=int(input("Ingrese otro número: "))
z=int(input("Ingrese un tercer número: "))

if x>y and x>z and y>z:
    print(z, y, x)
if x>y and x>z and z>y:
    print(y, z, x)
if y>x and y>z and x>z:
    print(z, x, y)
if y>x and y>z and z>x:
    print(x, z, y)
if z>x and z>y and x>y:
    print(y, x, z)
if z>x and z>y and y>x:
    print(x, y, z)
    