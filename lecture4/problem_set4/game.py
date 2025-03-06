
import random


def main():
    n = getLevel()
    guess(answer(n))

def answer(n):
    return random.randrange(1, n + 1)

def guess(number):
    
    while True:
        try:
            numGuess = int(input("Guess: "))
            if numGuess <= 0:
                raise ValueError
            break  # Exit the loop if input is valid
        except ValueError:
            ...
    if numGuess == number:
        print("Just right!")
    elif numGuess < number:
        print("Too small!")
    else:
        print("Too large!")

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