grocery = []
count = 0
while True:
    try:
        items = input().upper()
        grocery.append(items)
        for i in grocery:
            if i in grocery:
                count +=1
                grocery.append(count)
    except EOFError:
            return str(count, i, end='\n')







