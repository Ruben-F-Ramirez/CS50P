import sys



class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity



    def __str__(self):
        n = int(self.size)
        cookies = "🍪" * n
        return f"{cookies}"

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError
        else:
            self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError
        try:
            if capacity < 1:
                raise ValueError
            else:
                self._capacity = capacity
        except ValueError:
            sys.exit("Invalid capacity")

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,n):
        self._size = n

def main():
    testJar = Jar()
    print(testJar.size)
    print(testJar.capacity)
    testJar.deposit(5)
    print(testJar)
    testJar.withdraw(1)
    print(testJar)


if __name__ == "__main__":
    main()