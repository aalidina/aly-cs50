
def main():
    shorten(input)

def shorten(word):
    vowels = ["a","e","i","o","u"]
    input1 = input("Input: ").lower()
    for c in input1:
        if c in vowels:
            return ""
            # print("", end="")
        else:
            return c
            # print(c, end="")
    print(" ")


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


