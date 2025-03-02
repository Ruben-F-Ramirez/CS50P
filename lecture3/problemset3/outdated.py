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



def main():
    while True:
        try:
            old_date = input("Enter date in the format MM/DD/YYYY or September 1, 2025\n").capitalize()
            old_date = refine_date(old_date)
            month, day, year = old_date.split()
            try:
                if month.isnumeric():
                    month = int(month)
                if (1 <= month <= 12 and 1 <= int(day) <= 31):
                    convert_date(month, day, year)
                    break
            except TypeError:
                pass
            if 1 <= int(day) <= 31:
                month = months.index(month)
                convert_date(month, day, year)
                break
            

        except ValueError:
            pass

def refine_date(date):
    return date.replace("/", " ").replace(",", "")


def convert_date(month, day, year):
    print(f"{year}/{month:02}/{day:02}")

main()