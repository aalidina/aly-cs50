grocery = []
while True:
    try:
        items = input().upper()
        grocery += items
    except EOFError:
        # for i in grocery:
        print(str(grocery), end='\n')
        break


