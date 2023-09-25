fuel = input("Enter Fraction: ").split("/")
x,y = fuel

a = float(x)
b = float(y)
if a/b <= 1:
    print("E")
elif a/b >= 99:
    print("F")



