
def main():
    while True:
        try:
            num, denom = input("Fraction: ").split(sep= '/')
        except (ValueError, ZeroDivisionError):
            pass
    
    percent_tank(prompt)

def percent_tank(prompt):
    ...

main()