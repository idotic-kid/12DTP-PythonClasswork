students = ["zach"]
grades = [[]]

def ask(q, opt1, opt2, opt3="none", opt4="none"):
    print(q)
    print("Options:")
    print("[a] "+opt1)
    print("[b] "+opt2)
    if opt3!="none":
        print("[c] "+opt3)
    if opt4!="none":
        print("[c] "+opt4)
    return input()

def getstudent(sname):
    if sname in students:
        print()
    return

while True:
    output = ask("What would you like to do?","Write to list","Read from list")

    if output == "a": # Path for writing to list
        print()
    elif output =="b":
        print()
    else:
        print("Invalid input.")