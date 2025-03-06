
import inflect
import sys


p = inflect.engine()
names = []

def main():
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            say_adieu(names)
            #altsayAdieu(names)
            break


def say_adieu(names):
    print("Adieu, adieu to " + p.join(names))

def altsayAdieu(names):
    for i, name in enumerate(names, 1):
        if i == 1:
            print("Adieu, adieu, to " + name, end="")
        elif i == len(names):
            print(" and " + name)
        else:
            print(", " + name, end="")

main()