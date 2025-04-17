
def meow(n: int) -> str:
    """
    Meow n times

    :param n: number of times to print meow
    :type n: int
    :raise TypeError if n is not an int
    :return: return string of n lines of meow
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))

meows: str = meow(number)
print(meows, end="")

