grocery = []
count = 0
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery.append(items)
        for i in grocery:

    except EOFError:
        break
    print(i, end='\n')



