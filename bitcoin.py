
import requests
import sys
from sys import argv



# args = sys.argv[1:]


print(len(sys.argv[1]) )
# arg = float(sys.argv[1])

if len(sys.argv) <= 1:
     sys.exit("Missing Command Line Argument")
elif len(sys.argv[1]) > 2:
     sys.exit("Command-line argument is not a number")

# try:
#      amount = float(sys.argv[1]) * 38761.0833
#      print(f"${amount:,.4f}")
# except ValueError:
#      print("Command-line argument is not a number")



# arg = float(sys.argv[1])





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


