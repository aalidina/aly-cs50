while True:
    try:
        items = input("Enter Items: ").upper()
        grocery = []
        grocery += items
        for i in grocery:
            print(i, end = '\n')
    except EOFError:
        break
