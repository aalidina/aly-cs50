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
while True:
    date = input("Enter Date month day year or MM/DD/YYYY: ")
    if date == "," or "/":
        try:
            month,day,year = date.split("/")
            year = year.replace(" ","")
            # Check if month is between 1 and 12 and day is between 1 and 31
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            pass
            try:
                old_month,old_day,year = date.split(" ")
                for i in range(len(months)):
                    if old_month == months[i]:
                        month = i + 1
                # Remove comma from day variable
                day = old_day.replace(",", "")
                if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                    break
            except:
                print()
                pass

print(f"{year}-{int(month):02}-{int(day):02}")
