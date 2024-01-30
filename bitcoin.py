
import requests

number = float(input("Enter number of Bitcoin: "))

try:
    if number == " ":
        print("Missing command-line argument")
    elif number != int:
        print("Command-line argument is not a number")
    else:
        amount = number * 38761.0833
        print(f"${amount:,.4f}")
except requests.RequestException:
    print("Missing Command Line Argument")
