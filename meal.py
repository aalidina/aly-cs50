
# Structure your program per the below, wherein
def main():
    time = input("What time is it? ").split(":")
    convert(time)
    # print(hours)
    if convert(time) > 7:
        print("breakfast time")




def convert(time):
# convert is a function (that can be called by main) that converts time, a str in 24-hour format,
# to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

    h, m = time

    a = float(h)
    b = float(m)

    global hours
    hours = a + b / 60

    # print(hours)




if __name__ == "__main__":
    main()