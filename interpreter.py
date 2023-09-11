interpreter = input("Expression: " ).split(" ")

x,y,z = interpreter


a = float(x)
b = float(z)

if y == "+":
    print(a + b)
elif y == "-":
    print(x - z)
elif y == "/":
    print(x/z)
else:
    print(x*z)
