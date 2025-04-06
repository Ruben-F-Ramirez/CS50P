# pip install inflect


import inflect
p = inflect.engine()
import sys

from datetime import date

class Seasons:
    def __init__(self, dob):
        self.dob = dob
        self.today_date = date.today()

    def life_minutes(self, count) -> str:
        return p.number_to_words(count, andword="") + " " + p.plural_noun('minute', count)

    
    @staticmethod
    def get_dob() -> str:
        try:
            dob =  input("Date of Birth: ")
            return Seasons(date.fromisoformat(dob))
        except ValueError:
            sys.exit("Invalid date")

    def convert_date(self):
        days_lived = (self.today_date - self.dob).days
        return days_lived*24*60



def main():
    userDob = Seasons.get_dob()
    minutes = userDob.convert_date()
    result = userDob.life_minutes(minutes)
    print(result)


if __name__ == "__main__":
    main()