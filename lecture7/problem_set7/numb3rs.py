import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    

def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        pass
    else:
        return False
    for group in matches.groups():
        if 0 <= int(group) <= 255:
            pass
        else:
            return False
    return True
    

if __name__ == "__main__":
    main()