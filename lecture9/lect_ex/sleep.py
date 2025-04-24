# Prints n sheep

def main():
    n = int(input("What's n? "))
    for s in sheep:
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
