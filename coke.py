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

def change(c):
    if c > 50:
        print("Change Owed:", c - 50)
    elif c == 50:
        print("Change Owed:", 0)
    else:
        print("Amount Due:", 50 - c)
    return(c)

main()