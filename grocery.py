grocery = []
count = 0
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery.append(items)

    except EOFError:
        for i in grocery:
            print(i, end='\n')
            print(grocery)
            break



