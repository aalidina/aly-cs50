def main():

    g = fuel_gauge()
    print(f"{g}")

def fuel_gauge():
    while True:
        fuel = input("Enter Fraction: ").split("/")
        try:
            x,y = fuel
            a = float(x)
            b = float(y)

            if a/b * 100 == 0:
                return "E"
            elif a/b * 100 == 1:
                return "F"
            elif a/b * 100 == 75:
                return "75%"
            elif a/b * 100 == 25:
                return "25%"
            elif a > b:
                text = input("Fraction: ")


        except (ValueError, ZeroDivisionError):
            print("x is not an integer")
        else:
            return fuel





main()