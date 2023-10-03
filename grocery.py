grocery = {}
count = 0
while True:
    try:
        item = input().upper()
        if item in grocery:
            # count +=1
            # grocery.append(count)
            grocery[item] += 1
    except EOFError:
        for i in grocery:
            print(grocery[i], i, end='\n')
        break







