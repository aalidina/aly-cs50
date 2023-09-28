def main():

    g = fuel_gauge("Enter Fraction: ")
    print(f"{g}")

def fuel_gauge(prompt):
    while True:

        try:
            n,d = input(prompt).split("/")
            r = int(n)/int(d)

            if r > 1:
                continue
            elif r == 1/100 or r == 0/100:
                return "E"
            elif r  == 1 or r == 99/100:
                return "F"
            else:
                print(round(r * 100), '%', sep='')

        except (ValueError, ZeroDivisionError):
            pass
        else:
            break






main()