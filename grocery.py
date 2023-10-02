grocery = []
while True:
    try:
        items = input("Enter Items: ").upper()
        grocery += items
    except EOFError:
        # for i in grocery:
        print(grocery, end="\n")
        break

