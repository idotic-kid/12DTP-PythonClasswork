from easygui import *

def validate_float_input(question):
    i = False
    question_marks = "?"
    while i == False:
        i_str = enterbox(f"{question}{question_marks}", "Shopping List/numbah")
        try:
            i = float(i_str)
        except:
            if i_str != None:
                msgbox("I meant like a NUMBER", "Shopping List/you BIG IDIOT!")
                question_marks = question_marks+"?"
            else:
                msgbox("no cancelling😡", "Shopping List/possible misclick!?")
    return i

def add_item(the_list, mod):

    # "mod" is a parameter that stores the menu output, being
#("Add item", "Remove item", "Change price of item", "Change quantity of item")
    # operation_real is set to this so that the value can be changed later

    # Creates a temporary list variable with the uncommited modifications
    # Is always set to the original shopping list but ig if you wanted to have 
    # multiple shopping lists lol

    templist = the_list


    if mod =="Add item":


        try:
            new_item = enterbox("Enter the name of this item",
            "Shopping List/Entering new item").lower()
        except:
            msgbox("Oh okay then 😔", "Shopping List/possible misclick!?")
            return the_list


        if new_item in the_list: #fail
            msgbox("You already have this item in your shopping list!",
            "Shopping List/big dementia")
        else: #Succeed
            templist[new_item] = {"price":validate_float_input("How much does it cost (each)"),"quantity":validate_float_input("How much of this item do you want to add")}
    
    else:

        if len(the_list) >= 2:
            new_item = choicebox(f"Which item do you want to {mod}?",
        "Shopping List/editing the thing", list(the_list.keys()))
        else:
            new_item = list(the_list.keys())[0]
            a = buttonbox(f"Youve selected {new_item} cuz thats the only item",
            "Shopping List/youre so poor",("damn okay", "no what lemme leave"))
            if a == "no what lemme leave":
                msgbox("damn okay then :+1:", "Shopping List/ escape")
                return the_list


        if new_item not in the_list:
            msgbox("You don't HAVE that item in your shopping list!",
            "Shopping List/big dementia 2")
        else:
            if mod=="Remove item":
                templist.pop(new_item)
                msgbox(f"Successfully removed {new_item}!",
                "Shopping List/killing vegetables")

            elif mod =="Change price of item":
                old_price = templist[new_item]["price"]
                templist[new_item]["price"] = validate_float_input("Enter the NEW price of the item (each)!")
                msgbox("Successfully changed the price of {} from {} to {}!".format(new_item, old_price, templist[new_item]["price"]))

            elif mod=="Change quantity of item":
                old_amount = templist[new_item]["quantity"]
                templist[new_item]["quantity"] = validate_float_input("Enter the NEW amount of the item!")
                msgbox("Successfully changed the amount of {} in the shopping list from {} to {}!".format(new_item, old_amount, templist[new_item]["quantity"]))



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
    shopping_list_string = "⟪ ꜱʜᴏᴘᴘɪɴɢ ʟɪꜱᴛ ⟫"
    if isrange:
        minimum_price = validate_float_input("Enter minimum price:\n> ")
        maximum_price = validate_float_input("Enter maximum price:\n> ")
    
    if len(list) != 0:
        for i in list:
            if isrange:
                if list[i]["price"] > minimum_price and list[i]["price"] < maximum_price:
                    shopping_list_string = shopping_list_string + (" - {}x {}: ${} each".format(list[i]["quantity"], i, list[i]["price"]))
            else:
                shopping_list_string = shopping_list_string + ("\n - {}x {}: ${} each".format(list[i]["quantity"], i, list[i]["price"]))
    else:
        shopping_list_string = shopping_list_string + "\n There are no items \
in your shopping list."
    
    msgbox(shopping_list_string, "Shopping List/View List")


shopping_list = {"banana":{"price":3.5,"quantity":4}}



while True:
    menu_option = buttonbox("What would you like to do?", "Shopping List",
    ("Edit your shopping list", "View from your shopping list"))
    
    if menu_option == "Edit your shopping list": # Path for writing to list
        while menu_option !="5":
            menu_option = buttonbox("How would you like to edit your shopping \
                list?", "Shopping List/Edit",
                ("Add item", "Remove item", "Change price of item",
                "Change quantity of item", "Go back"))
            
            if menu_option != None and menu_option != "Go back":
                add_item(shopping_list, menu_option)
            else:
                break
            
            

    elif menu_option == "View from your shopping list": # Path for reading list
        display_list(shopping_list, False)


    else:
        msgbox("You can't do that.", "Shopping List/Tried to escape")