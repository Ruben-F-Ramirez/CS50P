

def main():
    print_column(3)
    print_row(3)

def print_square(size):

    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")
        print()
        
def print_row(width):
    print("?" * width)

def print_column(height):
    print("#\n" * height, end="")

main()