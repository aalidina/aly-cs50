grocery = []
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery.append(items)
        for i in grocery:
            print(i, end='\n')
    except EOFError:
        break


