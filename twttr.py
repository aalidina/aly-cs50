vowels = ["a","e","i","o","u"]
input = input("Input: ")
for i in input:
    if i in vowels:
        x = i.lstrip()
        print(x, end="")
print(" ")
