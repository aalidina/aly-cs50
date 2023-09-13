
# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
# to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    time()




    # if h > 7 & h < 8:
    #     print("breakfast time")

    # print(time)


def convert(time):
      time = input("What time is it? ").split(":")
      h, m = time
      hours = h * 24
      print(hours)

# breakfast = "7:00 and 8:00"
# lunch = "12:00 and 13:00"
# dinner = "18:00 and 19:00"


if __name__ == "__main__":
    main()