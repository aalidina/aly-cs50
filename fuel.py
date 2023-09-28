def main():

    g = fuel_gauge("Enter Fraction: ")
    print(f"{g}")

def fuel_gauge(prompt):
    while True:

        try:
            n,d = input(prompt).split("/")
            r = n/d
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if r > 1:
                continue
            elif r == 1/100 or r == 0/100:
                return "E"
            elif r  == 1 or r == 99/100:
                return "F"
            elif a/b * 100 == 75:
                return "75%"
            elif a/b * 100 == 25:
                return "25%"





main()