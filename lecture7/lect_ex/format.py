import re

name = input("What's your name").strip()

# :=, is called a walrus operator
if matches:= re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")