import random

x = 0
while x <= 0:
    number = int(input("Enter a positive integrer: "))
    y = random.randint(1, 100)
    guess = input("Guess: ")
    if guess == y:
        print 
    x = number
    print(y)