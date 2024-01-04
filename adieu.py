import sys, inflect

p = inflect.engine()
list = []

while True:
    try:
        names = input("Name:")
        list.append(names)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(list)}")
        break


