
def main():
    input1 = input("Input: ")
    shorten(input1)

def shorten(word):
    vowels = ["a","e","i","o","u"]
    for c in input1:
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


