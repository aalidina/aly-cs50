
# def main():
#     text = input("Input: ").lower()
#     shorten(text)

# def shorten(word):
#     output = ""
#     vowels = ["a","e","i","o","u"]

#     for c in word:
#         print(c)
#         if not c in vowels[:]:
#             output += c
#     return output

def main():
    text = input("Input: ")
    shorten(text)

def shorten(word):
    #text = input("Input: ")
    l = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
    out = ""

    for i in word:
            if not i in l[:]:
                    out += i
    return out

if __name__ == "__main__":
    main()

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


