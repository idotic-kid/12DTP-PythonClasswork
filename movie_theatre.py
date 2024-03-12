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

    
def input_24h_time(messgga):
    isvalid = False
    while not isvalid:
        answe = enterbox(messgga)
        time_len = len(answe.replace(":",""))
        if answe and time_len == 4 and answe[2] == ":":
            try:
                answe2 = int(answe.replace(":",""))
                isvalid = True
                answe2 = str(answe2)[:2]+":"+str(answe2)[2:]
            except:
                msgbox("noo u did it bad")
        elif answe == None:
            return None
    return answe2


def validate_bookings(messsg):
    return integerbox(msg=messsg, lowerbound=0, upperbound=150)


def edit_single_movie(dictionary_of_movies, movie, option):
    input_function = {"genre":enterbox, "duration":integerbox,
    "showtime":input_24h_time, "bookings":validate_bookings}
    temp = dictionary_of_movies
    
    temp2 = input_function[option](f"Enter your new {option}!")
    if temp2!=None:
        temp[movie][option] = temp2
        msgbox(f"made the {option} of {movie} to {temp2}")
        return temp
    else:
        msgbox("Oh okay thats fine as well :c")
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
        movie_detial_lost = ["genre", "duration", "showtime", "bookings"]
        temp_dcik = dictionary_of_movies
        temp_dcik[chosen_movie] = {}

        for i in movie_detial_lost:
            older_temp_dci = temp_dcik
            temp_dcik = edit_single_movie(dictionary_of_movies, chosen_movie,i)

            if temp_dcik == older_temp_dci:
                msgbox("thing is cancelled!!!!")
                return dictionary_of_movies
        
        return temp_dcik


def search(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    message_string = chosen_movie + "\n"

    for i in dictionary_of_movies[chosen_movie]:
        message_string = f"{message_string}\n\t - {i.capitalize()}: {dictionary_of_movies[chosen_movie][i]}"

    msgbox(message_string)
    return dictionary_of_movies


def edit_showtime(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    if chosen_movie !=None:
        return edit_single_movie(dictionary_of_movies, chosen_movie,"showtime")
    else:
        return dictionary_of_movies


def edit_bookings(dictionary_of_movies):
    chosen_movie = choose_movie(dictionary_of_movies)
    if chosen_movie !=None:
        return edit_single_movie(dictionary_of_movies, chosen_movie,"bookings")
    else:
        return dictionary_of_movies


def display_dictionary(dictionary_of_movies):
    '''shows a mesagebo xwith  movies and its   informaiton!!'''

    dictionary_str = "Currently Showing - - - - -"
    for movie_name in list(dictionary_of_movies.keys()):
        dictionary_str = f"- {dictionary_str}\n {movie_name}: "
        for detail in list(dictionary_of_movies[movie_name].keys()):
            dictionary_str = f"{dictionary_str}\n\t- {detail.capitalize()}:\
 {dictionary_of_movies[movie_name][detail]} "
    msgbox(dictionary_str)
    return dictionary_of_movies


while True:
    options = {
    "Add new movie":add_movie,
    "Search movie":search,
    "Reschedule showtime":edit_showtime,
    "Edit Bookings":edit_bookings,
    "Showing Today":display_dictionary,
    "Exit":None
    }

    menu_option = buttonbox("What would you like to do?",
    "Main Menu", list(options.keys()))
    if menu_option:
        movies = options[menu_option](movies)
    else:
        msgbox("okay byebye thanks for using MOVIE THEATER DOT PY")
        exit()
    