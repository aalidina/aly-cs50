import random

level : int = -1
while level < 0:

    level = int(input("Level: "))

    level 1 = 5

    rand_num = random.randint(0, 5)
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

