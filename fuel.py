def main():

    g = fuel_gauge("Enter Fraction: ")
    print(f"{g}")

def fuel_gauge(prompt):
    while True:

        try:
            fuel = input(prompt).split("/")
            x,y = fuel
            a = int(x)
            b = int(y)

            if a/b * 100 == 0:
                return "E"
            elif a/b * 100 == 1:
                return "F"
            elif a/b * 100 == 75:
                return "75%"
            elif a/b * 100 == 25:
                return "25%"


        except (ValueError, ZeroDivisionError):
            print("x is not an integer")
        else:
            return fuel





main()