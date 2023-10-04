months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
try:
    #prompt user for date
    date = input("Enter Date month day year or MM/DD/YYYY: ").upper().split('/')
    m,d,y = date
    print(y + "-" + m + "-" + d)
except:
    break

    # for m in months:
    # if m.upper() == months:
    #     print("x")
        # else:
        #     print("y")