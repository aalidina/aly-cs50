import random



# def get_level():
choice: int = 0
score = 0
fail = 0
while choice <= 1 or choice > 3:

    try:
        level = int(input("Level: "))
    except Exception:
        pass
        # return level


# def main():
# level: int = get_level()
    i = 0
    while i < 2:

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


# main()
