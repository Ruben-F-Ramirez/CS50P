
import inflect
import sys


p = inflect.engine()

def main():
    while True:
        try:
            get_input()
        except EOFError:
            say_adieu()

def get_input():
    ...

def say_adieu():
    ...

main()