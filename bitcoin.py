
import requests
import sys






# if type(number) != int:
#     print("Command-line argument is not a number")
# elif number == "":
#     print("Missing Command Line Argument")
try:
    number = int(input("Enter number of Bitcoin: "))

    if type(number) != int:
         print("Command-line argument is not a number")
    else:
        amount = number * 38761.0833
        print(f"${amount:,.4f}")

except (ValueError, requests.RequestException):
    print("Missing command-line Argument")

