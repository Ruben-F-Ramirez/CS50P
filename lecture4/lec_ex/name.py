# command line arguments

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
""" try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments") """
