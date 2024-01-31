
import requests
import sys



args = sys.argv[1:]
number = float(input("Enter number of Bitcoin: "))
print(sys.argv[1])

if len(args) == 0:
     print("Missing Command Line Argument")
     sys.exit("Command-line argument is not a number")






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


