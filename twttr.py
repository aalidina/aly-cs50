vowels = ["a","e","i","o","u"]
input = input("Input: ")
for i in input:
    if i in vowels:
        x = str(i.lstrip())
        input.translate( { ord(x): None } ), end=""
        print(y)
print(" ")
