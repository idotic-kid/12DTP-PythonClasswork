from easygui import *


movies = {"The Shawshank Redemption":["Drama", 142, "22:00", 143],
"The Godfather":["Drama", 175, "15:30", 111],
"Back to the Future":["Comedy", 116, "12:00", 102],
"Spirited Away":["Family", 125, "9:30", 98],
"The Lion King":["Family", 125, "07:00", 123]}


options = {"Edit Genre":0, "Edit Duration":1,
    "Schedule showtime":2, "Edit bookings":3}


def menu_loop():
    option_that_was_selected = 6996874397549
    while option_that_was_selected != "Exit":
        pass
    pass

def edit_movie(genre=None, dur=None, showtime=None, bookings=None):
    '''This will edit at least one item of the list in the value thing'''
    
    pass

def edit_bookings():
    """ ask user for a number
    if the output is over 150 then make you do it again
    then edit"""

    edit_movie(bookings=integerbox("How many bookings are there now?",
    "Edit > Bookings", lowerbound=0, upperbound=150))
    pass

def search():
    pass



menu_loop()