import sys
import csv

def main():
    file_check()
    before = file_read()
    after = file_scourge(before)
    file_scourgified(after)

def file_scourgified(students):
    with open(sys.argv[2], "a",newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

def file_scourge(before_list):
    after_list = []
    for row in before_list:
        last, first = row['name'].split(",")
        after_list.append({'first': first.lstrip(), 'last': last, 'house': row['house']})
    return after_list

def file_read():
    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
        return students
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def file_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()