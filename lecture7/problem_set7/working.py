import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """
    expected input:
    9:00 AM to 5:00 PM
    9 AM to 5 PM
    9:00 AM to 5 PM
    9 AM to 5:00 PM

    converts input time format to 24 hour time format
    example:
    >>> convert(9:00 AM to 5:00 PM)
    0900 to 1700
    """
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s)
    if time:
        pass
    else:
        raise ValueError
    if time.group(3) == "AM":
        meridian = 0
    else:
        meridian = 12

    # convert first time
    hour1 = int(time.group(1)) + meridian
    if time.group(2) == None:
        minutes1 = 0
    else:
        minutes1 = int(time.group(2))

    # convert second time
    if time.group(6) == "AM":
        meridian = 0
    else:
        meridian = 12

    hour2 = int(time.group(4)) + meridian
    if time.group(5) == None:
        minutes2 = 0
    else:
        minutes2 = int(time.group(5))

    
    return f"{hour1:02}{minutes1:02} to {hour2:02}{minutes2:02}"


...


if __name__ == "__main__":
    main()