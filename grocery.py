while True:
    try:
        items = input("Enter Items: ").upper()
        grocery = []
        grocery += items
    except EOFError:
        # for i in grocery:
        print(grocery[1], end='\n')
        break

