import random

level = 1
while level >= 1 and level <= 3:
    user = int(input("Level: "))
    x = rand_num = random.randint(1, 9)
    y = rand_num = random.randint(1, 9)

i = 0
while i < 10:
    input = int(input(f"{x} + {y} = "))

result = x+y

