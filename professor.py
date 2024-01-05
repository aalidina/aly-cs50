import random

level = 1
while level >= 1 and level <= 3:
    user = input("Level: ")
    x = rand_num = random.randint(1, 9)
    y = rand_num = random.randint(1, 9)
    
    input = input(f"{x} + {y} = ")
