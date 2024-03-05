from easygui import *

def function_that_checks_whether_something_is_in_24h_format():
    cOCKaNDbALLtORTURE = True
    string_of_numbers = "0123456789"
    while cOCKaNDbALLtORTURE:
        failture=0
        penisanusimagine = enterbox("Enter when the show is in hh:mm!")
        for i in penisanusimagine:
            if i not in string_of_numbers and i!=":":
                msgbox("NO YOU BALLSACK grr")
                break
                       
    pass

def add_movie(movies_dictionary):
    #this might work if it works dont touch it cuz i dont remember
    selected_movie = enterbox("What movie do you want to add?")
    if selected_movie in movies_dictionary:
        msgbox("You already have that movie, silly!")
    else:
        edit_movie(selected_movie, movies_dictionary,
        genre=enterbox("Enter what genre!!", "add genre"),
        dur=integerbox("Enter how long the movie is(minutes)!", lowerbound=0,),
        showtime=function_that_checks_whether_something_is_in_24h_format(),
        bookings=integerbox("How many bookings are there?",
    "Edit > Bookings", lowerbound=0, upperbound=150)     )


        buttonbox(choices=["yah", "nah"])

    pass


def edit_movie(movie, movies_dictionary,
genre=None, dur=None, showtime=None, bookings=None):
    temp_dick = movies_dictionary
    temp_dick[movie] = {genre}
    
    return temp_dick

def choose_a_movie_from_the_movies_dictionary_list(movies_dictionary,
what_thing_in_the_movie_you_wanna_edit):
    penisballssexamongus = choicebox(f"Which movie do you wanna \
        edit the {what_thing_in_the_movie_you_wanna_edit} of?", "Choosing",
        list(movies_dictionary.keys()))
    return penisballssexamongus


def edit_bookings(movies_dictionary):
    """ ask user for a number
    if the output is over 150 then make you do it again
    then edit"""

    edit_movie(bookings=integerbox("How many bookings are there now?",
    "Edit > Bookings", lowerbound=0, upperbound=150))
    pass


def edit_showtime(movies_dictionary):
    '''same thng as editbooking but with idx 3 instead of idx2'''
    msgbox("edit showtime or something")
    pass


def search(movies_dictionary):
    msgbox("search or something idk")
    pass


def check_with_user(movies_dictionary):
    pass


movies = {"The Shawshank Redemption":["Drama", 142, "22:00", 143],
"The Godfather":["Drama", 175, "15:30", 111],
"Back to the Future":["Comedy", 116, "12:00", 102],
"Spirited Away":["Family", 125, "9:30", 98],
"The Lion King":["Family", 125, "07:00", 123]}


options_menu_list_of_options = {
    "Add a new movie":add_movie,
    "Search for a movie":search,
    "Reschedule a showtime":edit_showtime,
    "Change the number of bookings for the movie":edit_bookings,
    "Exit":exit
    }




#mainloop
while True:
    selected_option = buttonbox("What would you like to do",
    "select smt", list(options_menu_list_of_options.keys()))
    
    movies = options_menu_list_of_options[selected_option](movies)


