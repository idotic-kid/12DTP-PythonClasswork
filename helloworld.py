students = []
grades = []

def ask(q, opt1, opt2, opt3="none"):
    print(q)
    print("[a] "+opt1)
    print("[b] "+opt2)
    if opt3!="none":
        print("[c] "+opt3)
    return input()

