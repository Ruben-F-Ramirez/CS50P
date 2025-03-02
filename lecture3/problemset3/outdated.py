month = [
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
    date = get_input()
    convert_date()

def get_input() -> str:
    return input("Enter date in the format MM/DD/YYYY or September 1, 2025\n")

def convert_date():
    ...

main()