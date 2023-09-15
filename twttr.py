vowels = ["a","e","i","o","u"]
input = input("Input: ")
for i in input:
    if i in vowels:
        print(i.lstrip(), end="")
print(" ")
