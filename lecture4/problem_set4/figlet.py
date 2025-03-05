
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    check_valid()
    message = get_str()
    fig_out(message)

def fig_out(message):
    fig_list = figlet.getFonts()
    if len(sys.argv) == 1:
        index = random.randrange(start=len(fig_list)-1)
        figlet.setFont(font=fig_list[index])
        print(figlet.renderText(message))
    elif len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(message))



def get_str():
    return input("Input: ")

def check_valid():
    val =  len(sys.argv)
    match val:
        case 1:
            ...
        case 3:
            if sys.argv[2] not in figlet.getFonts():
                print("Invalid usage")
                sys.exit
            elif sys.argv[1] == "-f":
                ...
            elif sys.argv[1] == "--font":
                ...
            else:
                print("Invalid usage")
                sys.exit
        case _:
            print("Invalid usage")
            sys.exit
    

main()