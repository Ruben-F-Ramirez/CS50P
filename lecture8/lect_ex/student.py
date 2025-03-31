
def main():
    student = get_student()
    if student['name'] == "Padmae":
        student['house'] = "Ravenclaw"
    
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {'house': house, 'name': name}

if __name__ == "__main__":
    main()