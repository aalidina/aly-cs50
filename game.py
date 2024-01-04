import random

x : int = -1
while x < 0:
    level = int(input("Level: "))
    y = random.randint(0, level)

    guess: int = -1

    while 1:
        guess = int(input("Guess: "))

        if guess > 0 and guess < level:

            if guess < y:
                print("Too small!")
            elif guess > y:
                print("Too large!")
            elif guess == y:
                print("Just right!")
                break
