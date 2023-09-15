c = 0
total = 0
print("Amout Due: 50")
while c < 50:
    coin = int(input("Insert Coin: "))
    c = coin + c
    if c > 50:
        print("Change Owed:", c - 50)
    else:
        print("Amount Due:", 50 - c)

