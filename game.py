import random

level : int = -1
while level < 0:
    try:
        level = int(input("Level: "))

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






