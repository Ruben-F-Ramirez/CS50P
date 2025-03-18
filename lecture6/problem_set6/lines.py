import sys



def main():
    file_check()
    line_count = file_read()
    print(line_count)


def file_read():
    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    pass
                elif line.isspace():
                    pass
                else:
                    count += 1
            return count
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