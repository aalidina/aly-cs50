import sys, inflect

x = []
while True:
    names = input("Name:")
    x.append(names)
    print("Adieu, adieu, to", x[0])
    print(inflect("Output:" + (input), language='alias'))