x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))

p1 = (x1, y1)
p2 = (x2, y2)
s = round((y2 -y1)/(x2-x1),5)

print("The slope for the line that connects two points ",p1, " and ",p2, " is ",s)
