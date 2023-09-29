menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    x = price()
    print(f"{x}")


def price():
    total = 0
    while 1:
        # item = input("Item: ").lower()
        item: str = input("Item: ").lower()
        try:
            for item in menu:
                total += menu[item]
                    # // Print the new total formatted to 2 decimal points
                print("$" + f"{total:.2f}")
                break
            else:
                return total


        # // Except Control+D is pressed
        except EOFError:
            return total


main()