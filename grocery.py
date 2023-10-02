grocery = []
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery += items
    except EOFError:
        # for i in grocery:
        print(str(grocery), end='\n')
        break
    else:
        break

