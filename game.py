import random

level : int = -1
while level < 0:
    try:
        level = int(input("Level: "))

        level1 = random.randint(0, 5)
        level2 = random.randint(5, 10)
        level3 = random.randint(10, 15)

        rand_num = random.randint(1, level)
        guess: int = -1
        while True:

            guess = int(input("Guess: "))

            if guess > 0 and guess <= 5:

                if guess <  rand_num:
                    print("Too small!")
                elif guess >  rand_num:
                    print("Too large!")
                elif guess ==  rand_num:
                    print("Just right!")
                    break

    except ValueError:
        pass






