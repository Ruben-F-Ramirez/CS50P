import sys
import csv

from tabulate import tabulate

def main():
    file_check()
    p_list = read_menu()
    p_table = table_menu(p_list)
    print(p_table)
    

def read_menu():
    pizzas = []  
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            pizzas.append({"pizza": row[0], "small": row[1], "large": row[2]})
    return pizzas

def table_menu(table):
    return tabulate(table, headers="firstrow", tablefmt="grid")

def file_check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")



if __name__ == "__main__":
    main()