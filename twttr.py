vowels = ["a","e","i","o","u"]
input = input("Input: ")
for c in input:
    if c in vowels:
       print("", end="")
    else:
        print(c, end="")
print(" ")


