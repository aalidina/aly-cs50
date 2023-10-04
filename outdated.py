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

#prompt user for date
date = input("Enter Date month day year or MM/DD/YYYY: ").split()
m,d,y = date
if m in months:
    print(ymd)
else:
    print(y + "-" + m + "-" + d)