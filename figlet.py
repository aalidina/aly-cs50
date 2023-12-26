from pyfiglet import Figlet
import sys

if sys.argv[1] not in ["-f","--font"]:
    sys.exit("Invalid usage")
input = input("Enter Text: ")
