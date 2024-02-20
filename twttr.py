
def main():
    input = input("Input: ")
    shorten(input)

def shorten(word):
    vowels = ["a","e","i","o","u"]
    for c in input:
        if c in vowels:
            print("", end="")
        else:
            print(c, end="")
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


