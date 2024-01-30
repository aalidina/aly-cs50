import random

def main():

    # choice: int = 0
    problems = 0
    score = 0
    chances = 3
    lvl = get_level()
    while problems < 10:
        if chances == 3:
            x, y = generate_integer(lvl)
        try:
            math = int(input(f"{x} + {y} = "))
            result = x+y

            if math == result:
                score += 1
                problems += 1
                chances = 3
                continue
            elif math != result:
                chances += - 1
                print("EEE")
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances += - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {x+y}"))
            chances = 3
            problems -= -1
            continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except Exception:
            pass


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