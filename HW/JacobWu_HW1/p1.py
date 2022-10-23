import math

w = float(input("Enter the width of a rectangle: "))
h = float(input("Enter the height of a rectangle: "))

p = 2*(w+h)
a = w*h
d = math.sqrt(w*w + h*h)

print("The perimeter is " + str(p))
print("The area is " + str(a))
print("The length of the diagonal is " + str(d))
