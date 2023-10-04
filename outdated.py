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
date = input("Enter Date month day year or MM/DD/YYYY: ").upper().split("/,")
m,d,y = date
print(m)
for m in months:
    date.split(",")
    if m.upper() == months:
        print("x")
    # else:
    #     print("y")