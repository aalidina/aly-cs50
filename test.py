def main():
    x = menu()
    return x

def menu():
    while True:
        try:
            item = input("Item: ").lower()
            for i in menu:
                if item == i.lower():
                    print("$" + f"{menu[i]}")
        except EOFError:
            pass
        else:
            return "x"

menu()