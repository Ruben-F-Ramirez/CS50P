import re

url = input("URL: ").strip()

if mathches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE):
    print(f"username is {mathches.group(1)}")