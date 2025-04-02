class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter
    @property
    def house(self):
        return self.house
    
    #setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError
        self.house = house

def main():
    student = get_student()
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except:
        ...

if __name__ == "__main__":
    main()