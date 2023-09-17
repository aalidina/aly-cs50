vowels = ["a","e","i","o","u"]
input = input("Input: ")
for i in input:
    if i in vowels:
        x = str(i.lstrip())
        # y = input.translate(x)
        print(input.translate(x))
print(" ")


txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))