import random

level = 1
while level >= 1 and level <= 3:
    user = int(input("Level: "))


    i = 0
    right = 0
    wrong = 0
    while i < 10:
        x = rand_num = random.randint(1, 9)
        y = rand_num = random.randint(1, 9)
        math = input(f"{x} + {y} = ")
        result = x+y
        i += 1
        if math == result:
            right += 1
        elif math != result:
            wrong += 1
    break
print(f"total score {right}")
print(right)

