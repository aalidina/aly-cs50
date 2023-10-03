grocery = []
count = 0
while True:
    try:
        items = input().upper()
        for i in grocery:
            if i in grocery:
                count +=1
                grocery.append(count,items)
                print(count, i, end='\n')
    except EOFError:
        print(i)





