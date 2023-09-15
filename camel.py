case = input("camleCase: ")
for i in case:
    if i.islower():
        print(True, end="")
    else:
        print(case, end="")