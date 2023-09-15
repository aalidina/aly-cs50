vowels = ["a","e","i","o","u"]
input = input("Input: ")
for i in input:
    if i in vowels:
        x = str(i.lstrip())
        print(x.lstrip(input), end="")
print(" ")
