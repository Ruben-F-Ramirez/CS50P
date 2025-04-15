
class Cat:
    MEOWS = 3

    def __init__(self):
        pass

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

def main():
    cat = Cat()
    cat.meow()


if __name__ == "__main__":
    main()