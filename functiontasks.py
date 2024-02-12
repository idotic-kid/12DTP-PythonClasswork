# task 1: Write a function that takes two
#         numbers as arguments and returns the sum.
def ballsack(num1,num2):
    return num1+num2


# task 2: Write a function that takes a list of numbers
#         as an argument and returns the largest number in the list.
def biggestinlist(inputlist):
    return max(inputlist)


# task 3: Write a function that takes a string as an
#         argument and returns the number of vowels in the string.
def vowelcount(inputstr):
    numofvowels = 0
    vowels = "aeiouAEIOU"

    for i in inputstr:
        if i in vowels:
            numofvowels+=1
    return numofvowels


# task 4: Write a function that takes two strings as
#         arguments and returns True if the second string is
#         identical to the first, and False otherwise.
def samestr(str1,str2):
    if str1==str2:
        return True
    else:
        return False


# task 5: Write a function that takes a list of strings as
#         an argument and returns a new list containing only
#         the strings that have a length greater than 3 characters.
def morethan3(inputlist):
    outputlist = []
    for i in inputlist:
        if len(i) > 3:
            outputlist.append(i)
    return outputlist


# task 6: Write a function that takes a number as an argument
#         and returns True if the number is even, and False otherwise.
def iseven(inputnum):
    if inputnum%2 == 0:
        return True
    else:
        return False


# task 7: Write a function that takes two lists of numbers
#         as arguments and returns a new list containing the
#         elements that are common to both lists.
def similaritems(inputlist1, inputlist2):
    outputlist = []
    for i in inputlist1:
        if i in inputlist2:
            outputlist.append(i)
    return outputlist
