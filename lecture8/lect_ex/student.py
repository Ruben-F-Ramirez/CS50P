class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError
        self.name = name
        self.house = house

        def __str__(self):
            return "A student"



def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()