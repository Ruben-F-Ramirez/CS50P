

def main():
    groceries = {}

    while True:
        try:
            get_item(groceries)
        except EOFError:
            sort_items(groceries)
            break

def get_item(groceries):
    item = input().upper()

    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item] = 1

def sort_items(groceries):
    for i in sorted(groceries):
        print(f"{groceries[i]} {i}")

main()