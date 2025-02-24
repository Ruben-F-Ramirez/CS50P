

def main():
    prompt = get_prompt()
    twttfy(prompt)
# get user string
def get_prompt():
    return input("Enter your string: ")
# remove vowels from string
def twttfy(prompt):
    for c in prompt:
        if c.lower != "a" or c.lower != "e" or c.lower != "i" or c.lower != "o" or c.lower != "u":
            print(c, end="")

main()