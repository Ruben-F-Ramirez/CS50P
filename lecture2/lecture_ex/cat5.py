

def main():
    meow(get_number())

def get_number():
    while True:
        n = input("What's n?")
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()