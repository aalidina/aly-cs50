interpreter = input("Expression: " ).split(" ")

x,y,z = interpreter


a = float(x)
b = float(z)

if y == "+":
    print(a + b)
elif y == "-":
    print(a - b)
elif y == "/":
    print(a / b)
else:
    print(a * b)
