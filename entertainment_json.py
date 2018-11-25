import fresh_tomatoes as ft
import json
import movies

# loading data from the json file with movie details
with open('movies_details.json', 'r') as file:
    movies_data = json.load(file)

movie_title = ''
movie_storyline = ''
poster_image = ''
trailer_youtube = ''
movies_list = []


def show_movies():
    """
    Displays all the movies.

    Prints all the movies that are currently available in the system.
    To let the user decide if they want to add more movies or not.
    """
    print('The movies website currently has {} movies. The following:\n'.format(len(movies_data['movies'])))
    for i in range(len(movies_data['movies'])):
        print('{}. {}'.format(i+1, movies_data['movies'][i]['movie_title']))


def add_movies():
    """
    Add new movies.

    Gives option to user to add new movies.
    If they want to add, gives option to enter the
    title of the movie, and the links to the poster
    and YouTube trailer, and the story line.

    Returns
    -----------------
    choice: bool
        whether any new movie has been added or not
    """
    choice = input('\nShould we add more movies? Y/N  ').lower()
    add_movies = choice
    if add_movies == 'yes' or add_movies == 'yus' or add_movies == 'y':
        print('\nAlright! Lets add few more movies')
        number = 1
        while add_movies == 'yes' or add_movies == 'yus' or add_movies == 'y':
            movie_title = input('For movie number {}, enter the Title.  '.format(number)).title()
            movie_storyline = input('\nThe story line for this movie.  ')
            poster_image = input('\nLink for the movie poster.  ')
            trailer_youtube = input('\nYouTube link for its trailer.  ')

            new_movie = {'movie_storyline': movie_title,
                         'movie_title': movie_title,
                         'poster_image': poster_image,
                         'trailer_youtube': trailer_youtube}
            movies_data['movies'].append(new_movie)
            print('Saved this one!')
            add_movies = input('\nAdd another one? Y/N  ').lower()
            number += 1
    if choice == 'yes' or choice == 'yus' or choice == 'y':
        choice = True
    else:
        choice = False
    return choice


def save_movies():
    """
    Option to save new movies in the system.

    If the user has queried for new movies, it gives the option to
    add those movies to the JSON we maintain, so those movies show up
    everytime without needing to add them later.
    """
    save_movies = input('Save these movies permanently? Y/N  ')
    if save_movies == 'yes' or save_movies == 'yus' or save_movies == 'y':
        with open('movies_details.json', 'w') as file:
            json.dump(movies_data, file)


def display_trailer_webpage():
    """
    Display the final trailer webpage.

    Reads the JSON file with old and new (if added) movies
    and prepares the webpage with trailers of all the movies.
    """
    for i in range(len(movies_data['movies'])):
        name = movies_data['movies'][i]['movie_title']
        movie_title = name
        movie_storyline = movies_data['movies'][i]['movie_storyline']
        poster_image = movies_data['movies'][i]['poster_image']
        trailer_youtube = movies_data['movies'][i]['trailer_youtube']
        # adding object each time to the list of movie objects
        movies_list.append(movies.Movies(movie_title, movie_storyline, poster_image, trailer_youtube))

    # using fresh_tomatoes.py file to finally open the webpage with the movie object items
    ft.open_movies_page(movies_list)


def main():
    """
    Main function to controll all other functions from one place.

    Handles all functions at one place and lets users have option to add new movies.
    If they add new movies, gives options to save new movies' data permanently.
    Retrieves all the movies' data using pythn API module or API url.
    Displays the movies trailer webpage.
    """
    # display current stored movies
    show_movies()

    # option to add new movies
    if add_movies():
        save_movies()

    # display trailer webpage
    display_trailer_webpage()


if __name__ == "__main__":
	main()
