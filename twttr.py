
def main():
    text = input("Input: ").lower()
    shorten(text)

def shorten(word):
    output = ""
    vowels = ["a","e","i","o","u"]

    for c in word:
        if not c in vowels[:]:
            output += c
    print(output)
    return output




    # vowels = ["a","e","i","o","u"]
    # input = input("Input: ")
    # for c in input:
    #     if c in vowels:
    #         print("", end="")
    #     else:
    #         print(c, end="")
    # print(" ")

if __name__ == "__main__":
    main()


