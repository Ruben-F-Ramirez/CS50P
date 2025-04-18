#a program using the argparser library
#to pass arg flags


import argparse

parser = argparse.ArgumentParser(description="meow like a cat")

parser.add_argument("-n",default=1,type= int,help="number of meows")

args = parser.parse_args()
meows = "meow\n" * args.n
print(meows,end="")