import random

level = 1
while level >= 1 and level <= 3:
    user = int(input("Level: "))


    i = 0
    while i < 9:
        x = rand_num = random.randint(1, 9)
        y = rand_num = random.randint(1, 9)
        math = input(f"{x} + {y} = ")
        i += 1
        print(i)
        break
    result = x+y

