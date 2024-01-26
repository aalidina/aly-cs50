import random

def main():
    i = 10
    choice: int = 0
    score = 0
    fail = 0
    lvl = get_level()
    while i != 0:

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

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except Exception:
            pass
            # return level

if __name__ == "__main__":
    main()