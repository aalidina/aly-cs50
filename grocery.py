grocery = {}
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery += items
        print(grocery, end='\n')
    except EOFError:
        # for i in grocery:
        break


