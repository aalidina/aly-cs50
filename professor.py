import random

def main():
    i = 0
    choice: int = 0
    score = 0
    fail = 0
    chance = 3
    lvl = get_level()
    while i < 10:
        if chance == 3:
            x, y = generate_integer(lvl)
        try:
            math = int(input(f"{x} + {y} = "))
            result = x+y
            i += 1

            if math == result:
                score += 1
            elif math != result:
                fail += 1
        except ValueError:
            print("EEE")
            pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except Exception:
            pass
            # return level

def generate_integer(level):
    if level == 1:
        x = rand_num = random.randint(0, 9)
        y = rand_num = random.randint(0, 9)
    elif level == 2:
        x = rand_num = random.randint(10, 99)
        y = rand_num = random.randint(10, 99)
    elif level == 3:
        x = rand_num = random.randint(100, 999)
        y = rand_num = random.randint(100, 999)
    return x,y

if __name__ == "__main__":
    main()