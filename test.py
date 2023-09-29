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



total = 0
while True:
    item = input("Item: ").lower()
    try:
        for i in menu:
            if item == i.lower():
                total += menu[i]
                    # // Print the new total formatted to 2 decimal points
                print("$" + f"{total:.2f}")
                # print(item)
                # print(i.lower())
            else:
                return "x"

    # // Except Control+D is pressed
    except EOFError as e:
        return item


main()