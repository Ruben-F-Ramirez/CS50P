
from pyfiglet import Figlet
import sys
import random

def main():
    check_valid()
    message = get_str()
    fig_out()

def fig_out():
    ...

def get_str():
    return input("Input: ")

def check_valid():
    if len(sys.argv) == 0:
        ...
    elif len(sys.argv) == 2:
        ...
    else:
        print("Invalid usage")
        sys.exit
    

main()