
# Structure your program per the below, wherein
def main():
    x = input("What time is it? ")
    x = convert(x)
    if 7 <= x <=8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("Lunch Time")
    elif 18 <= x <= 19:
        print("Dinner Time")




def convert(time):
# convert is a function (that can be called by main) that converts time, a str in 24-hour format,
# to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

    h, m = time.split(":")

    a = float(h)
    b = float(m)

    time = a + b / 60
    return(time)





if __name__ == "__main__":
    main()