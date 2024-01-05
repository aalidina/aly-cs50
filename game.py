import random

level = int(-1)
while level < 0:
    level = int(input("Level: "))
    rand_num = random.randint(0, level)

    guess: int = -1

    while 1:
        guess = int(input("Guess: "))

        if guess > 0 and guess < level:

            if guess <  rand_num:
                print("Too small!")
            elif guess >  rand_num:
                print("Too large!")
            elif guess ==  rand_num:
                print("Just right!")
                break


