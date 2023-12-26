from pyfiglet import Figlet
import sys

if sys.argv[1] not in ["-f","-font"]:
    sys.exit("Invalid usage")

input = input("Enter Text: ")


# // Initialize figlet modules
figlet = Figlet()
figlet.getFonts()

# // Set the figlet font
figlet.setFont(font = sys.argv[2])

# // Print the rendered text
print(figlet.renderText(inp))