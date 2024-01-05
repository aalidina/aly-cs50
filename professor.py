import random

level = 1
score = 0
fail = 0
while level >= 1 and level <= 3:
    user = int(input("Level: "))


    i = 0
    while i < 10:

        x = rand_num = random.randint(1, 9)
        y = rand_num = random.randint(1, 9)
        math = int(input(f"{x} + {y} = "))
        result = x+y
        i += 1

        if math == result:
            score += 1
        elif math != result:
            fail += 1
            print("EEE")

    break
print(f"total score {score}")

