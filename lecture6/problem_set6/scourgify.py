import sys
import csv

def main():
    file_check()

def file_read():
    try:
        students = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "home": row["home"]})

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"{student['name']} is from {student['home']}")
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