import sys, inflect

p = inflect.engine()
x = []
while True:
    try:
        names = input("Name:")
        x.append(names)

    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(x)}")
