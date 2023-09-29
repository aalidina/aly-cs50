menu = {
    "Baja Taco": "4.00",
    "Burrito": "7.50",
    "Bowl": "8.50",
    "Nachos": "11.00",
    "Quesadilla": "8.50",
    "Super Burrito": "8.50",
    "Super Quesadilla": "9.50",
    "Taco": "3.00",
    "Tortilla Salad": "8.00"
}

def main():

    x = price()
    print(f"{x}")




def price():
    while True:
        item = input("Item: ").lower()
        try:
            for i in menu:
                if item == i.lower():
                    return str("$" + f"{menu[i]}")
        except EOFError:
            pass

        return item

main()