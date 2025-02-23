# using packages

# use pip install in terminal to install packages
# ex: pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow('Hello World' + sys.argv[1])