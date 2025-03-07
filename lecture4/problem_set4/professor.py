
import random


def main():
    n = get_level()
    score = 0

    for i in range(0, 10):
        x = generate_integer(n)
        y = generate_integer(n)

        for j in range(0, 3):
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                score += 1
                break
            else:
                print("EEE")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level >3:
                    raise ValueError
            return level
        except ValueError:
            pass
    


def generate_integer(digits):
    return random.randint(1, (10 ** digits) - 1)


if __name__ == "__main__":
    main()