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
    templist = list
    print(templist)
    #remember to .lower() the input item name
    # list[input("item name").lower()] = {"price":validate_str_to_float(),"quantity":validate_str_to_float_()}
    return

def total_price(list):
    total = 0
    for i in list.values():
        total += i['price']*i['quantity']
    return total

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
                if list[i]["price"] > minimum_price and list[i]["price"] < maximum_price:
                    print(" - {}x {}: ${}".format(list[i]["quantity"], i, list[i]["price"]))
            else:
                print(" - {}x {}: ${}".format(list[i]["quantity"], i, list[i]["price"]))
    else:
        print("There are no items in your shopping list.")


shopping_list = {"banana":{"price":3.5,"quantity":4}}



while True:
    menu_option = input("What would you like to do?\n[1] Add one item to shopping list\n[2] Calculate total price of shopping list\n[3] Check price of item in list\n[4] Display full shopping list\n[5] Display items within a specified price range\n> ")
    
    if menu_option == "1":
        print("no code here yet")
        shopping_list = add_item(shopping_list)

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