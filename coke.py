def main():
    c = 0
    d = [5, 10, 25]
    print("Amout Due: 50")
    while c < 50:
        coin = int(input("Insert Coin: "))
        if coin in d:
            c = coin + c
            change(c)
        else:
            print("Amount Due:", 50)

def change(coin):
    if coin > 50:
        print("Change Owed:", coin - 50)
    elif coin == 50:
        print("Change Owed:", 0)
    else:
        print("Amount Due:", 50 - coin)
    return(coin)

main()