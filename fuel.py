def main():

    g = fuel_gauge()
    print(f"{g}")

def fuel_gauge():
    while True:
        try:
            fuel = input("Enter Fraction: ").split("/")
            x,y = fuel
            a = float(x)
            b = float(y)

            if a/b * 100 == 0:
                print("E")
            elif a/b * 100 == 1:
                print("F")
            elif a/b * 100 == 75:
                print("75%")
            elif a/b * 100 == 25:
                print("25%")
        except ValueError:
            print("x is not an integer")
        else:
            return fuel






main()