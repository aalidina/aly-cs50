interpreter = input("Expression: " ).split(" ")

x,y,z = interpreter

a = float(x)
b = float(z)

if y == "+":
    print(a + b)
# elif y[1] in interpreter:
#     print(x - z)
# elif y[2] in interpreter:
#     print(x + z)
else:
    print(x * z)
