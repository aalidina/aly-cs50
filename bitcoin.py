
import requests
import sys
import json
from sys import argv


def main():
     value = req_coin() # Assigning the value of req_coin to value
     if len(sys.argv) < 2: # Checking if an argument was passed when running python.bitcon.py
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






