
import random


def main():
    n = getLevel()
    guess(answer(n))

def answer():
    ...

def guess():
    ...

def getLevel():
    while True:
        try:
            num = int(input("Level: "))
            if num <= 0:
                raise ValueError
            return num  # Exit the loop if input is valid
        except ValueError:
            ...

main()