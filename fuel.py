try:
    g = fuel_gauge()
    print(f"{g}")

except ValueError:
    pass
else:



def fuel_gauge()
    fuel = input("Enter Fraction: ").split("/")
    x,y = fuel
    a = float(x)
    b = float(y)

    if a/b * 100 <= 0.01:
        print("E")
    elif a/b * 100 >= 0.99:
        print("F")


