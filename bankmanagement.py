user = "bob"
account_balance = 1200

def deposit(bal, dep_amount):
    try:
        return int(bal) + int(dep_amount)
    except:
        return "fail"

def withdraw(bal, withdraw):
    if int(withdraw) <= int(bal):
        return bal - withdraw
    else:
        return "fail"

def check_balance(bal):
    return "Your balance is $"+str(bal)


while True:
    prompt = input("hey bob what do u wanna do\n[1] deposit\n[2] withdraw\n[3] check balance\n")

    if prompt =="1":
        temp = deposit(account_balance, input("enter deposit amount\n"))
        if not "fail" in temp:
            account_balance=temp
            print("Transaction successful. Balance updated to $"+str(account_balance))
        else:
            print("Transaction failed")

    elif prompt=="2":
        temp = withdraw(account_balance, input("enter withdrawal amount\n"))
        if not "fail" in temp:
            account_balance=temp
            print("Transaction successful. Balance updated to $"+str(account_balance))
        else:
            print("Transaction failed.")

    elif prompt=="3":
        print(check_balance(account_balance))

    else:
        print("Invalid option.")
