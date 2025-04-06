# pip install inflect


import inflect
p = inflect.engine()

from datetime import date


def main():
    delta = convert_date(get_birthday())
    print(life_minutes(delta))

def life_minutes(count) -> str:
    return p.number_to_words(count, andword="")

def convert_date(date1) -> int:
    today = date.today.minutes
    delta = today - date1.minutes()
    return delta

def get_birthday() -> str:
    return input("Date of Birth: ")


if __name__ == "__main__":
    main()