try:
    fuel = input("Enter Fraction: ").split("/")
    x,y = fuel
    a = float(x)
    b = float(y)
except ValueError:
    pass
else:

    if a/b * 100 <= 0.01:
        print("E")
    elif a/b * 100 >= 0.99:
        print("F")

    # def fuel_gauge()
    #     empty = a/b * 100


