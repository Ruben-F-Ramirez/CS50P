import re

url = input("URL: ").strip()

mathches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if mathches:
    print(f"username is {mathches.group(3)}")