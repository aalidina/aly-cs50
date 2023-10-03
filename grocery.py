grocery = []
count = 0
while True:
    try:
        items = input().upper()
        grocery.append(items)
        for i in grocery:
            print(i, end='\n')
    except EOFError:
        print(i)
        break



