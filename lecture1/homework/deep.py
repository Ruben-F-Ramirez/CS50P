# Author: Ruben Ramirez
# Date: Feb 8, 2025
#
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two 
# or forty two. Otherwise output No.

# function that compares input to 42 or (case-insensitively) forty-two 
# or forty two
def answer(n):
    if n == "42" or "forty-two" or "forty two":
        print("yes")
    else:
        print("no")

# a main function
def main():
    question = "What is the answer to the Great Question of Life, \
    the Universe and Everything"

    text = input(question)

    answer(text.lower())

main()