
import requests

number = float(input("Enter number of Bitcoin: "))
if number != int:
    print("Command-line argument is not a number")
elif number == "":
    print("Missing Command Line Argument")
try:
    amount = number * 38761.0833
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("Missing Command Line Argument")

