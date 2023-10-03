grocery = {}

while True:
    try:
        item = input("").upper()
        if item in grocery:
            grocery[item] += 1
    except EOFError:
        for i in sorted(grocery):
            print(grocery[i], i)
        break







