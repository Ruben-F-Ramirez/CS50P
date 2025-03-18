import sys
import csv

def main():
    file_check()
    file_read()

def file_scourgified(students):
    for student in students:
        with open(sys.argv[2], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
            writer.writerow({"first name": student['first_name'], "last name": student['last_name'], "house": student['house']})

def file_scourge():
    ...

def file_read():
    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
        for student in students:
            print(f"{student['name']} is from {student['house']}")
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