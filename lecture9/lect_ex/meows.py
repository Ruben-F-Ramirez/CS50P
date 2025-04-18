import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n: int = int(sys.argv[2])
    print("meow\n" * n,end="")
else:
    print("Usage: meows.py")