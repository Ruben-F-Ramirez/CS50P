# A simple program using match to place young wizards in their house

name = input("What is your name?\n")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?  That's not a wizard I've heard of.")
