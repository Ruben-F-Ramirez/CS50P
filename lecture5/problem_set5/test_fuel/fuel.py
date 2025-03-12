def main():
    while True:
        try:
            percent = convert(input("Fraction: "))
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        print(gauge(percent))


def convert(fraction: str) -> int:
        num, denom = fraction.split(sep= '/')
        if num.isdigit() is False:
            raise ValueError
        if denom.isdigit() is False:
            raise ValueError
        if denom == "0":
            raise ZeroDivisionError
        if int(num) > int(denom):
            raise ValueError
        return round(int(num) / int(denom) * 100)

def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()