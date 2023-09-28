def main():

    g = fuel_gauge("Enter Fraction: ")
    print(f"{g}")

def fuel_gauge(prompt):
    while True:

        try:
            n,d = input(prompt).split("/")
            r = int(n)/int(d)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if r > 1:
                continue
            elif r == 1/100 or r == 0/100:
                return "E"
            elif r  == 1 or r == 99/100:
                return "F"
            elif r == 75:
                return "75%"
            elif r == 75:
                return "75%"
            print(round(r * 100), '%', sep='')
            break





main()