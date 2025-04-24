# Prints n sheep

def main():
    n = int(input("What's n? "))
    for s in sheep:
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
