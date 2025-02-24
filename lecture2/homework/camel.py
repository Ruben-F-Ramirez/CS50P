# problem set 2 camel case

# get user input
def main():
    prompt = snake(input("camel case: "))

# change camel case to snake case
# ex: firstName -> first_name
def snake(camel):
    print("snake case: ", end="")
    for c in camel:
        if c.isupper():
            print(f"_{c.lower()}", end="")
        else:
            print(c, end="")

main()