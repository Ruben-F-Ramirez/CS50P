# get user fruit label
def main():
        
# create dictionary of fruit names: calories
    fruits_dict = {'apple':'130', 'avocado':'50', 'banana': '110', 'cantaloupe': '50', 'grapefruit': '60',\
                    'grapes': '90', 'honeydew': '50', 'kiwifruit': '90', \
                    'lemon': '15', 'lime': '20', 'nectarine': '60', 'orange': '80',\
                    'peach': '60', 'pear': '100', 'pineapple': '50', 'plums': '70', \
                    'strawberries': '50', 'sweet': '100', 'sweet cherries': '100', \
                    'tangerine': '50', 'watermelon': '80'}

    while True:
        fruit = input("Item: ").lower()
        if fruit in fruits_dict:
            break
    print("Calories: " + fruits_dict[fruit])

main()