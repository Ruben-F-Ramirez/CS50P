"""
a program using the argparser library
to pass arg flags
"""


import argparse

parser = argparse.ArgumentParser(description="meow like a cat")

parser.add_argument(-n,help="number of meows")

args = parser.parse_args()

