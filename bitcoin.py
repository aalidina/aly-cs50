
import requests
import sys
import json
from sys import argv




# result = float(usd) * float(gcoin)
# #     print(gcoin)
# #     print(f"${result:,.4f}")


def main():
     value = req_coin() # Assigning the value of req_coin to value
     if len(sys.argv) <= 1: # Checking if an argument was passed when running python.bitcon.py
          sys.exit("Missing Command Line Argument") #Exit if no argument was passed

     try:
          amount = float(sys.argv[1]) * value #multiple the number of bitcoin by bitcoin current price
          print(f"${amount:,.4f}")
     except ValueError: # If there is a ValueError exist the program and print the message.
          sys.exit("Command-line argument is not a number")


def req_coin():
     req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") # calling rest api to get bitcoin value
     data = req.json()
     usd = data["bpi"]["USD"]["rate_float"]
     return usd


main()



# if type(number) != int:
#     print("Command-line argument is not a number")
# elif number == "":
#     print("Missing Command Line Argument")
# try:
#     number = float(input("Enter number of Bitcoin: "))
#     # print(sys.argv[1])

#     if type(number) != float:
#          sys.exit("Command-line argument is not a number")
#     else:
#         amount = number * 38761.0833
#         print(f"${amount:,.4f}")


# except (ValueError, requests.RequestException):
#      sys.exit("Command-line argument is not a number")


