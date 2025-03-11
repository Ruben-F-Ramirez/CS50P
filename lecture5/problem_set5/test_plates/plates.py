
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if check_length(s):
        pass
    else:
        return False
    return check_alpha_pre(s[0:1]) and check_punct(s) \
    and check_num_end(s)

def check_alpha_pre(s: str) -> bool:
    if s.isalpha():
        return True
    return False
    
def check_length(s: str):
    if 2 <= len(s) <= 6:
        return True
    return False

def check_punct(s: str) -> bool:
    if s.isalnum():
        return True
    return False

def check_num_end(s: str) -> bool:
    digit = False
    if s.isalpha():
        return True
    for c in s:
        if not digit and c == '0':
            return False
        if (digit and c.isalpha()):
            return False
        if c.isdecimal():
            digit = True
    return digit

if __name__ == "__main__":
    main()