

def main():
    prompt = get_prompt()
    twttfy(prompt)
# get user string
def get_prompt():
    return input("Enter your string: ")
# remove vowels from string
def twttfy(prompt):
    for c in prompt:
        if (c.lower() != 'a' and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u" ):
            print(c, end="")

main()