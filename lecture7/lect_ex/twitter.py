

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")

print(f"username is {username}")