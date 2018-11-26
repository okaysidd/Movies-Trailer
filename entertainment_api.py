import tmdbsimple as tmdb
import urllib
import fresh_tomatoes as ft
import json
import movies
import webbrowser


tmdb.API_KEY = '9ee394eab0a844afcd7dbf8af77bded5'


with open('movies_details.json', 'r') as file:
    json_movies_data = json.load(file)


# to save all movie titles to inform user if adding some movie twice
movie_titles = []
for i in range(len(json_movies_data['movies'])):
    movie_titles.append(json_movies_data['movies'][i]['movie_title'])


def show_movies():
    """
    Displays all the movies.

    Prints all the movies that are currently available in the system.
    To let the user decide if they want to add more movies or not.
    """
    print('The movies website currently has {} movies.')
    print('The following:\n'.format(len(json_movies_data['movies'])))
    for i in range(len(json_movies_data['movies'])):
        title_of_movie = json_movies_data['movies'][i]['movie_title']
        print('{}. {}'.format(i+1, title_of_movie))


def search_for_movie():
    """
    Add new movies.

    Gives option to user to add new movies.
    If they want to add, looks up the movies mentioned using the tmdb API
    and returns the top 3 results with their names and the date of release.
    Else goes ahead with displaying the movies webpage in the next function.

    Returns
    -----------------
    movie object
        returned from the API and contains movie details,
        such as title, id and release date

    """
    while True:
        movie_name = input('\nWhich movie should we add to the trailers webpage?\n')  # noqa

        # initiating search method
        search = tmdb.Search()
        response = search.movie(query=movie_name)
        movies_list = search.results

        if len(movies_list) == 0:
            print('No such movie found :(')
            print('Lets try again')
            continue

        # if only one search result with the movie name
        if len(movies_list) == 1:
            print('Is this the movie you meant?')
            title_of_movie = movies_list[0]['title']
            release_date = movies_list[0]['release_date']
            print('{} - release date- {}'.format(title_of_movie, release_date))
            movie_picked = input('Y/N  ').lower()
            if movie_picked == 'yes' or movie_picked == 'yus' or movie_picked == 'y':  # noqa
                movie_picked = movies_list[0]
                return movie_picked

        # if search returned more than one result for the movie name
        number = 1
        print('\nWhich movie did you mean?')
        print()
        for s in movies_list[:3]:
            title_of_movie = s['title']
            release_date = s['release_date']
            print('{}. {} -- release in {}'.format(str(number), title_of_movie, release_date))  # noqa
            number += 1
        print()
        print('{}. None of these'.format(str(number)))
        movie_choice = input('Enter a number..  ')

        if movie_choice == '4':
            continue
        elif movie_choice == '':
            print('That\'s an invalid input.')
            continue
        elif movie_choice in '123' and int(movie_choice) <= number:
            movie_picked = movies_list[int(movie_choice)-1]
            return movie_picked
        else:
            print('That\'s an invalid input.')
            continue


def get_youtube_link(movie_picked):
    """
    Get the YouTube link to the movie trailer.

    The API result returned from the tbdb python module usually
    does not have the YouTube trailer link in the parameters.
    This funtion takes the movie id and uses the url for the API
    to get the YouTube link to the trailer of the movie.

    Parameters
    ---------------------
    arg1: string
        id (in string format) of the movie of which the YouTube
        trailer is required.

    Returns
    ---------------------
    string
        key of the YouTube link that can be used to generate the
        whole trailer link.
    """
    link = 'https://api.themoviedb.org/3/movie/' + movie_picked + '/videos?api_key=' + tmdb.API_KEY + '&language=en-US'  # noqa
    try:
        source = urllib.request.urlopen(link)
    except:
        print('Something went wrong. Maybe check the internet connection?\n')

    # getting the movie data in json format from the http request format that the above api returns  # noqa
    data = source.read().decode("utf-8")
    jmovie_data = json.loads(data)
    youtube_link_key = jmovie_data["results"][0]['key']
    youtube_link = 'https://www.youtube.com/watch?v=' + youtube_link_key
    return youtube_link


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
            json.dump(json_movies_data, file)


def display_trailer_webpage():
    """
    Display the final trailer webpage.

    Reads the JSON file with old and new (if added) movies
    and prepares the webpage with trailers of all the movies.
    """
    movies_list = []
    for i in range(len(json_movies_data['movies'])):
        name = json_movies_data['movies'][i]['movie_title']
        movie_title = name
        movie_storyline = json_movies_data['movies'][i]['movie_storyline']
        poster_image = json_movies_data['movies'][i]['poster_image']
        trailer_youtube = json_movies_data['movies'][i]['trailer_youtube']

        # adding object each time to the list of movie objects
        movies_list.append(movies.Movies(movie_title, movie_storyline, poster_image, trailer_youtube))  # noqa

    # using fresh_tomatoes.py file to finally open the webpage with the movie object items  # noqa
    ft.open_movies_page(movies_list)


def main():
    """
    Main function to controll all other functions from one place.

    Handles all functions at one place and lets users have option to add new movies.  # noqa
    If they add new movies, gives options to save new movies' data permanently.
    Retrieves all the movies' data using pythn API module or API url.
    Displays the movies trailer webpage.
    """
    try:
        source = urllib.request.urlopen('https://www.google.com/')
    except:
        print('Your internet connection might not be working.')
        print('You won\'t be able to add new movies if the internet connection doesn\'t work.')  # noqa
        print('The movies webpage might not work as intended')
        print('The links to the YouTube trailer won\'t work.')
        input('Click enter to continue..  ')
        display_trailer_webpage()
        return

    show_movies()

    new_movie_added = False

    while True:

        choice = input('\nAdd more movies? Y/N  ').lower()

        if choice == 'yes' or choice == 'yus' or choice == 'y':
            # search for the movie the user wants and get its id
            movie_picked = search_for_movie()
            # print(movie_picked)
            movie_title = movie_picked['title']

            if movie_title in movie_titles:
                print('A movie with the same name already exists.')
                ch = input('Continue to add? Y/N  ').lower()
                if ch != 'yes' and ch != 'yus' and ch != 'y':
                    continue

            movie_storyline = movie_picked['overview']
            poster_path = str(movie_picked['poster_path'])
            poster_image = 'https://image.tmdb.org/t/p/original' + poster_path
            # webbrowser.open(movie_poster)

            # getting the youtube link and the storyline from the json response of the api  # noqa
            trailer_youtube = get_youtube_link(str(movie_picked['id']))

            # create object of the movie and add to the json retrieved
            new_movie = {
                'movie_storyline': movie_storyline,
                'movie_title': movie_title,
                'poster_image': poster_image,
                'trailer_youtube': trailer_youtube
            }
            json_movies_data['movies'].append(new_movie)

            print('Added this movie.')

            new_movie_added = True

            print()

        else:

            break

    if new_movie_added:
        save_movies()

    display_trailer_webpage()


if __name__ == '__main__':
    main()
