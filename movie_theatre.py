from easygui import *


movies = {
"The Shawshank Redemption":{"genre":"Drama","duration":142, "showtime":"22:00", "bookings":143},
"The Godfather":{"genre":"Drama","duration":175, "showtime":"15:30", "bookings":111},
"Back to the Future":{"genre":"Comedy","duration":116, "showtime":"12:00", "bookings":102},
"Spirited Away":{"genre":"Family","duration":125, "showtime":"09:30", "bookings":98},
"The Lion King":{"genre":"Family","duration":125, "showtime":"07:00", "bookings":123}
}


def choose_movie(dictionary_of_movies):
    return choicebox("What movie do u want","choose a movie",
    list(dictionary_of_movies.keys()))
    
def validate_24h_time():

    pass

def edit_single_movie(dictionary_of_movies, movie, option):
    input_function = {"genre":enterbox, "duration":integerbox,
    "showtime":validate_24h_time, "bookings":integerbox}
    temp = dictionary_of_movies
    
    temp[movie][option] = input_function[option](f"Enter your new {option}!")
    msgbox(f"old list is {dictionary_of_movies} new list is{temp}")
    return temp


def add_movie(dictionary_of_movies):
    '''Asks user for a movie, if the movie is already in the list show
    other options and executes it if selected (otherwise go back to main
    menu) else (not in list) will ask users for details and add it to movie'''


    chosen_movie = enterbox("What's the name of the movie you want to add?")

    if chosen_movie in dictionary_of_movies:
        msgbox("That movie is already in the list!")
        extra_options = {"Reschedule its showtime":"showtime",
    "Change the number of bookings for the movie":"bookings",
    "Change the genre of the movie":"genre"}
        
        try: 
            return edit_single_movie(dictionary_of_movies, chosen_movie,
        extra_options[choicebox("Would you like to edit that movie instead?",
        "redo", list(extra_options.keys()))])
        except:
            msgbox("Oh alright then that's fine as well")
            return dictionary_of_movies

    else:
        pass

    pass



def search(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    pass

def edit_showtime(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    edit_single_movie(dictionary_of_movies, chosen_movie, "showtime")
    pass

def edit_bookings(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    edit_single_movie(dictionary_of_movies, chosen_movie, "bookings")

    pass

def display_dictionary(dictionary_of_movies):
    dictionary_string = "Currently Showing"
    for i in list(dictionary_of_movies.keys()):
        dictionary_string = f"{dictionary_string}\n {i}: "
        for a in dictionary_of_movies[i]:
            dictionary_string = f"{dictionary_string} {a} "
    msgbox(dictionary_string)
    return dictionary_of_movies


while True:
    options = {
    "Add a new movie":add_movie,
    "Search for a movie":search,
    "Reschedule a showtime":edit_showtime,
    "Change the number of bookings for the movie":edit_bookings,
    "Show the list of movies showing right today":display_dictionary,
    "Exit":exit
    }

    menu_option = buttonbox("What would you like to do?",
    "Main Menu", list(options.keys()))

    movies = options[menu_option](movies)
    