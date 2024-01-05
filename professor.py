import random

level = 1
right = 0
wrong = 0
while level >= 1 and level <= 3:
    user = int(input("Level: "))


    i = 0
    while i < 1:

        x = rand_num = random.randint(1, 9)
        y = rand_num = random.randint(1, 9)
        math = int(input(f"{x} + {y} = "))
        result = int(x+y)
        i += 1

        if math == result:
            right += 1
            print(right)
        elif math != result:
            wrong += 1
        print(f"total score {right}")
        print(right)
    break


