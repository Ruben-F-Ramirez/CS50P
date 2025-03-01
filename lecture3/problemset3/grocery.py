

def main():
    groceries = {}

    while True:
        try:
            get_item(groceries)
        except EOFError:
            sort_items(groceries)
            break

def get_item(items):
    item = input().upper()

    if item in items:
        items[item] += 1
    else:
        items[item] = 1

def sort_items(list):
    for i in sorted(list):
        print(f"{list[i]} {i}")

main()