def validate_str_to_float(question):
    i = False
    question_marks = "?"
    while i == False:
        i_str = input(f"{question}{question_marks}\n> ")
        try:
            i = float(i_str)
        except:
            print("I meant like a NUMBER (in dollars)")
            question_marks = question_marks+"?"
    return i

def add_item(list):
    price_float = 69420
    item = input("What item would you like to add?\n> ").lower()
    question_marks = "?"
    if item in list:
        return "n/a"
    else:
        price_float = validate_str_to_float(f"How much does {item} cost")
        return item, price_float

def total_price(list):
    return sum(list.values())

def find_item(item, list):
    if item.lower() in list:
        return list[item.lower()]
    else:
        return False

def display_list(list, isrange):
    if isrange:
        minimum_price = validate_str_to_float("Enter minimum price:\n> ")
        maximum_price = validate_str_to_float("Enter maximum price:\n> ")
    
    print("⟪ ꜱʜᴏᴘᴘɪɴɢ ʟɪꜱᴛ ⟫")
    if len(list) != 0:
        for i in list:
            if isrange:
                if list[i] > minimum_price and list[i] < maximum_price:
                    print(" - {}: ${}".format(i, list[i]))
            else:
                print(" - {}: ${}".format(i, list[i]))
    else:
        print("There are no items in your shopping list.")

shopping_list = {}

while True:
    menu_option = input("What would you like to do?\n[1] Add one item to shopping list\n[2] Calculate total price of shopping list\n[3] Check price of item in list\n[4] Display full shopping list\n[5] Display items within a specified price range\n> ")
    
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
    
    elif menu_option =="4":
        display_list(shopping_list, False)
    
    elif menu_option=="5":
        display_list(shopping_list, True)
    else:
        print("Invalid option.")