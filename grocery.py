while True:
    try:
        items = input("Enter Items: ").upper()
        grocery = []
        grocery += items
    except EOFError:
        for i in grocery:
            print(i, end = '\n')
