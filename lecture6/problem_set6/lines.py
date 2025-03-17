import sys



def main():
    file_check()
    line_count = file_read()
    print(line_count)


def file_read():
    try:
        lines = 0
        with open(sys.argv[1]) as file:
            for line in file:
                lines += 1
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


def file_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")



if __name__ == "__main__":
    main()