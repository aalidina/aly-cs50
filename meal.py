def main():
    time = input("What time is it? ").split(":")

    h, m = time


    breakfast = "7:00 and 8:00"
    lunch = "12:00 and 13:00"
    dinner = "18:00 and 19:00"


    if h > 7 & h < 8:
        print("breakfast time")

    print(time)


def convert(time):
    ...


if __name__ == "__main__":
    main()