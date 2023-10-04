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
    date = input("Enter Date month day year or MM/DD/YYYY: ").upper()
    if "/" in date:
        m,d,y = date.split("/")
        print(y + "-" + m + "-" + d)
    elif "," in date:
        m,d,y = date.split(",")
        m = (months.index(m) + 1)
        print(m)
except:
    pass