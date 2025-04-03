class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # getter
    @property
    def name(self):
        return self._name
    @property
    def house(self):
        return self._house
    
    #setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError
        self._house = house

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