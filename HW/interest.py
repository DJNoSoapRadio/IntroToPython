i = float(input("Enter investment amount: "))
r = float(input("Enter annual interest rate: "))
y = float(input("Enter number of years: "))
a = round(i * (1+ r / 12 / 100)**12*y, 2)
print(str(a))

