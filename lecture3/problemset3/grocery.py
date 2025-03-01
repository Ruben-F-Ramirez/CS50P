

def main():
    groceries = {}

    while True:
        try:
            item = input().upper()

            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1


        except EOFError:
            sort_items
            break

def sort_items(list):
    for i in sorted(list):
        print(i)

main()