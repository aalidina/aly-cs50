
def main():
    input1 = input("Input: ").lower()
    shorten(input1)

def shorten(word):
    output = ""
    vowels = ["a","e","i","o","u"]

    for c in word:
        if c in vowels:
            if not i in l[:]:
                    output += i
            return output
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


