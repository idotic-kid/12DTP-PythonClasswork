def add_item(item, price, list):
    if item in list:
        return False
    else:
        try:
            price2 = float(price)
            return [item.lower(), price2]
        except ValueError: 
            return False

def total_price(list):
    return sum(list.values())

def find_item(item, list):
    if item.lower() in list:
        return list[item.lower()]
    else:
        return False


shopping_list = {}

while True:
    menu_option = input("What would you like to do?\n[1] Add item to shopping list\n[2] Calculate total price of shopping list\n[3] Check price of item in list\n> ")
    
    if menu_option == "1":
        new_item = add_item(input("What item would you like to add?\n> "), input("How much does this item cost?\n> "), shopping_list)
        if new_item == False:
            print("write a descriptive error message later")
        else:
            shopping_list[new_item[0]] = new_item[1]
            print("added {} to shopping list with price ${}".format(new_item[0], new_item[1]))

    elif menu_option == "2":
        print("Total price: $", total_price(shopping_list))
    
    elif menu_option =="3":
        item_price = find_item(input("Which item do you want to find?\n> "), shopping_list)
        if item_price != False:
            print("that item has a price of $", item_price)
    
    else:
        print("Invalid option.")