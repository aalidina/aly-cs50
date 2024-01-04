import random

x = 0
while x <= 0:
    number = int(input("Level: "))
    y = random.randint(1, 100)
    guess = int(input("Guess: "))
    While guess > 0:
        if guess < y:
            print("Too small!")
        elif guess > y:
            print("Too large!")
        else:
            print("Just right!")
