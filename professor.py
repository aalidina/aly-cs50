import random



def get_level():
level : int = 0
score = 0
fail = 0
    while level <= 1 or level > 3:

        try:
            level = int(input("Level: "))
        except Exception:
            pass
            return level



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

get_level()

