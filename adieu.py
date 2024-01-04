import sys, inflect

p = inflect.engine()
x = []

while 1:
    try:
        names = input("Name:")

        if len(names) < 1:
            sys.exit(0)

        x.append(names)

    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(x)}")

        break
