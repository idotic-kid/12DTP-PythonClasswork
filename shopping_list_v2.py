def validate_str_to_float(question):
    i = False
    question_marks = "?"
    while i == False:
        i_str = input(f"{question}{question_marks}\n> ")
        try:
            i = float(i_str)
        except:
            print("I meant like a NUMBER")
            question_marks = question_marks+"?"
    return i

def add_item(list, mod):

    # "mod" is a parameter that stores the menu output, being
    #[1] add [2] delete [3] change price [4] change quantity
    # operation_real is set to this so that the value can be changed later

    # Creates a temporary list variable with the uncommited modifications
    # Is always set to the original shopping list but ig if you wanted to have multiple shopping lists lol

    templist = list
    
    new_item = input("Enter the name of this item\n> ").lower()


    if mod == "1" and new_item in list:
        print("This item is already in your list. Perhaps you meant to do something else?")
        print("""[1] Back out to main menu
[2] Remove the item from the shopping list
[3] Change the price of the item
[4] Change the quantity of the item""")
        djfhfbdh = input("> ")


    else:
        operation_real = mod


    templist[new_item] = {"price":validate_str_to_float("How much does it cost"),"quantity":validate_str_to_float("How much of this item do you want to add")}
    return templist



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
    menu_option = input("What would you like to do?\n[1] Modify your shopping list\n[2] View from your shopping list\n> ")
    
    if menu_option == "1": # Path for writing to list
        while menu_option !="5":
            menu_option = input("""[<] Modify your shopping list
Options:
    [1] Add an item to your shopping list
    [2] Remove an item from your shopping list
    [3] Change the price of an item
    [4] Change the quantity of an item
    > """)
            if menu_option in "1234":
                add_item(shopping_list, menu_option)
            else:
                print("Bad input")
            
            

    elif menu_option == "2": # Path for reading from list
        menu_option = input("")


    else:
        print("Invalid option.")