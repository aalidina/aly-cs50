
def main():
    value(text)

def value(greeting):
    greeting = (input("Greeting: ")).lower().strip()
    if greeting.startswith("hello"):
       return "$0"
    elif greeting.startswith("h"):
        # print("$20")
        return "$20"
    else:
        # print("$100")
        return "$100"


if __name__ == "__main__":
    main()