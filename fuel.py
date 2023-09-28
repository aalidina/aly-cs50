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

            if a/b > 1:
                continue
            elif a/b * 100 == 0 or a/b * 100 == 0.01:
                return "E"
            elif a/b * 100 == 1 or a/b * 100 == 99:
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