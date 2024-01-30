
import requests

number = float(input("Enter number of Bitcoin: "))
try:
    amount = number * 38761.0833
    print(f"${amount:,.4f}")
except requests.RequestException:
    print()
