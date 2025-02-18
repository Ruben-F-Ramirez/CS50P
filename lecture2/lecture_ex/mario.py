

def main():
    print_column(3)
    print_row(3)

def print_row(width):
    print("?" * width)

def print_column(height):
    print("#\n" * height, end="")

main()