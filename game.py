import random

x = 0
while x <= 0:
    level = int(input("Level: "))
    y = random.randint(0, level)
    guess = int(input("Guess: "))

    while guess > 0:
        if guess < y:
            print("Too small!")
        elif guess > y:
            print("Too large!")
        else:
            print("Just right!")
