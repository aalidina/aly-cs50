def main():

    g = fuel_gauge("Enter Fraction: ")
    print(f"{g}")

def fuel_gauge(prompt):
    while True:

        try:
            n,d = input(prompt).split("/")
            r = n/d
        except (ValueError, ZeroDivisionError):
            print("x is not an integer")
        else:
            if r > 1:
                continue
            elif r == 0 or r == 99/100:
                return "E"
            elif a/b * 100 == 1 or a/b * 100 == 99:
                return "F"
            elif a/b * 100 == 75:
                return "75%"
            elif a/b * 100 == 25:
                return "25%"





main()