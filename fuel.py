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

        except ValueError:
            print("x is not an integer")
        else:
            return fuel






main()