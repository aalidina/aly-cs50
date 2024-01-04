import sys, inflect

p = inflect.engine()
x = []
while True:
    names = input("Name:")
    x.append(names)
    print(f"\nAdieu, adieu, to {p.join(names)}")
