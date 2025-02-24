

# prompt for user to deposit a single coin
def main():
    change = get_coin()
    print(f"Change Owed: {change}")
# calculate amount due
def get_coin():
    due = 50
    while due > 0:
        coin = int(input("Insert Coin: "))
        if coin == 10 or coin == 5 or coin == 25:
            due = due - coin
        if due <= 0:
            return -1 * due
        else:
            print(f"Amount Owed: {due}")

main()