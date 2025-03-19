import sys



def main():
    file_check()



def file_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith((".png",".jpeg",".jpg")):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()