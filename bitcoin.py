
import requests

number = float(input("Enter number of Bitcoin: "))

try:
    if number != int:
        print("Command-line argument is not a number")
    elif number == int:
        amount = number * 38761.0833
        print(f"${amount:,.4f}")
    else:
        raise ValueError
except requests.RequestException:
    print("Missing Command Line Argument")

# print("Missing Command Line Argument")