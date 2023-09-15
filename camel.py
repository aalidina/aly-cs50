case = input("camleCase: ")
for i in case:
    if i.islower():
        print(i, end="")
    else:
        print("_" + i.lower(), end="")
