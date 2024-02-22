def add_item(list):
    price_float = 69420
    item = input("What item would you like to add?\n> ").lower()
    question_marks = "?"
    if item in list:
        return "n/a"
    else:
        while price_float == 69420:
            price_str = input(f"How much does {item} cost{question_marks}\n> ")
            try:
                price_float = float(price_str)
            except:
                print("I meant like a NUMBER (in dollars)")
                question_marks = question_marks+"?"
        return item, price_float

def total_price(list):
    return sum(list.values())

def find_item(item, list):
    if item.lower() in list:
        return list[item.lower()]
    else:
        return False


shopping_list = {}

while True:
    menu_option = input("What would you like to do?\n[1] Add one item to shopping list\n[2] Calculate total price of shopping list\n[3] Check price of item in list\n> ")
    
    if menu_option == "1":
        new_item = add_item(shopping_list)
        if new_item == "n/a":
            print("That item is already in your shopping list.")
        else:
            shopping_list[new_item[0]]=new_item[1]
            print("Successfully added {} with cost of ${}".format(new_item[0], new_item[1]))

    elif menu_option == "2":
        print("Total price is $", total_price(shopping_list))
    
    elif menu_option =="3":
        item_price = find_item(input("Which item do you want to find?\n> "), shopping_list)
        if item_price != False:
            print("that item has a price of $", item_price)
        else:
            print("That item is not in your shopping list.")
    
    else:
        print("Invalid option.")