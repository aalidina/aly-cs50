import random

x = 0
while x <= 0:
    level = int(input("Level: "))
    y = random.randint(0, level)


    while 1:
        guess = int(input("Guess: "))

        if guess > 0 and guess < level:

            if guess < y:
                print("Too small!")
            elif guess > y:
                print("Too large!")
            else:
                print("Just right!")
                break
