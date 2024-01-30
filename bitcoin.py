
import requests
import sys






# if type(number) != int:
#     print("Command-line argument is not a number")
# elif number == "":
#     print("Missing Command Line Argument")
try:
    number = float(input("Enter number of Bitcoin: "))
    # print(sys.argv[1])

    if type(number) != float:
         print("Command-line argument is not a number")
    else:
        amount = number * 38761.0833
        print(f"${amount:,.4f}")


except (ValueError, requests.RequestException):
     print("Command-line argument is not a number")

