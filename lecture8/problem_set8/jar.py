import sys



class Jar:
    def __init__(self, capacity=12):
        try:
            if capacity < 0:
                raise ValueError
            self.capacity = capacity
        except ValueError:
            sys.exit("Invalid capacity")


    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    testJar = Jar(-1)


if __name__ == "__main__":
    main()