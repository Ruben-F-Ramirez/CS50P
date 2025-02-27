
def main():
    while True:
        fuel = input("Fraction: ")
        try:
            num, denom = fuel.split(sep= '/')
            num = int(num)
            denom = int(denom)
            percent = round(num / denom *100)
            if percent <= 100:
                break

        except (ValueError, ZeroDivisionError):
            pass
    
    percent_tank(percent)

def percent_tank(percent):
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

main()