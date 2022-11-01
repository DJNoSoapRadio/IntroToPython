import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b*b - 4*a*c

if (d > 0):
    r1 = (b*-1 + math.sqrt(d))/ (2*a)
    r2 = (b*-1 - math.sqrt(d))/ (2*a)
    print("The roots are ", r1, "and ", r2)
elif (d == 0):
    r = (b*-1)/ (2*a)
    print("The root is ", r)
else:
    print("The equation has no real roots")
