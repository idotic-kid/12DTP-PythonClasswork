## look at my very nice code

exitcondition = True

alaiz = [96, 80, 87, 92]
bob = [82, 44, 55, 23]
ishangupta = [99, 100, 98, 69]

def average(student):
    return "this guy's average grade is " + str(sum(student)/len(student))

def lowest(student):
    return "this guy's lowest grade is " + str(min(student))

def highest(student):
    return "this guy's highest grade is " + str(max(student))


while exitcondition:
    ans = input("Options:\n[a] Write grade to list\n[b] Read from list\n[c] End program\n")
    if ans =="a": # Branch for writing from list

        selected_student = input("Options:\n[a] alaiz\n[b] bob\n[c] ishan gupta\n")

        if selected_student == "a":
            alaiz.append(int(input("Write a grade to alaiz's grades\n")))

        elif selected_student == "b":
            bob.append(int(input("Write a grade to bob's grades\n")))

        elif selected_student == "c":
            ishangupta.append(int(input("Write a grade to ishan gupta's grades\n")))

        else:
            print("Not an option 😡")


    elif ans =="b": # Branch for reading from list
        option = input("Options:\n[a] Calculate student grade average\n[b] Display lowest grade of student\n[c] Display highest grade of student\n[d] Read a student's grades \n")

        if option=="a": # Average
            selected_student = input("Options:\n[a] alaiz\n[b] bob\n[c] ishan gupta\n")
            if selected_student == "a":
                print(average(alaiz))

            elif selected_student == "b":
                print(average(bob))

            elif selected_student == "c":
                print(average(ishangupta))

            else:
                print("this student isnt real")


        elif option=="b": # Lowest
            selected_student = input("Options:\n[a] alaiz\n[b] bob\n[c] ishan gupta\n")
            if selected_student == "a":
                print(lowest(alaiz))

            elif selected_student == "b":
                print(lowest(bob))

            elif selected_student == "c":
                print(lowest(ishangupta))

            else:
                print("this student isnt real")


        elif option=="c":
            selected_student = input("Options:\n[a] alaiz\n[b] bob\n[c] ishan gupta\n")
            if selected_student == "a":
                print(highest(alaiz))

            elif selected_student == "b":
                print(highest(bob))

            elif selected_student == "c":
                print(highest(ishangupta))

            else:
                print("this student isnt real")

        elif option=="d":
            selected_student = input("Options:\n[a] alaiz\n[b] bob\n[c] ishan gupta\n")
            if selected_student == "a":
                print(alaiz)

            elif selected_student == "b":
                print(bob)

            elif selected_student == "c":
                print(ishangupta)

            else:
                print("this student isnt real")

        else:
            print("Not a valid option 😡")

    elif ans =="c":
        exitcondition=False
    

    else:
        print("Invalid input.")

quit()