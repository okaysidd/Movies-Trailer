import fresh_tomatoes as ft
import json
import movies

# loading data from the json file with movie details
with open('movies_details.json','r') as file:
    movies_data = json.load(file)

movie_title = ''
movie_storyline = ''
poster_image = ''
trailer_youtube = ''
movies_list=[]

# displaying all the current movies' details in the json file
def show_movies():
    print('The movies website currently has {} movies. The following:\n'.format(len(movies_data['movies'])))
    for i in range(len(movies_data['movies'])):
        print('{}. {}'.format(i+1, movies_data['movies'][i]['movie_title']))

# choice to add new movies in the json file
def add_movies():
    choice = input('\nShould we add more movies? Y/N  ').lower()
    add_movies = choice
    if add_movies=='yes' or add_movies=='yus' or add_movies=='y':
        print('\nAlright! Lets add few more movies')
        number = 1
        while add_movies=='yes' or add_movies=='yus' or add_movies=='y':
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
    if choice=='yes' or choice=='yus' or choice=='y':
        choice = True
    else:
        choice = False
    return choice

# choice to save these movies permanently in the json file
def save_movies():
    save_movies = input('Save these movies permanently? Y/N  ')
    if save_movies=='yes' or save_movies=='yus' or save_movies=='y':
        with open('movies_details.json','w') as file:
            json.dump(movies_data,file)

# creating Movies() objects of all the movies present in the movies_details.json file, then displaying
def display_trailer_webpage():
    for i in range(len(movies_data['movies'])):
        name = movies_data['movies'][i]['movie_title']
        # formatting the movie title so that object name is always without spaces, and also makes sense
        #movie_title = ('_').join(name.split())
        movie_title = name
        movie_storyline = movies_data['movies'][i]['movie_storyline']
        poster_image = movies_data['movies'][i]['poster_image']
        trailer_youtube = movies_data['movies'][i]['trailer_youtube']
        # adding object each time to the list of movie objects
        movies_list.append(movies.Movies(movie_title, movie_storyline, poster_image, trailer_youtube))

    # using fresh_tomatoes.py file to finally open the webpage with the movie object items
    ft.open_movies_page(movies_list)

# main function to call all the above functions from
def main():
    # display current stored movies
    show_movies()

    # option to add new movies
    if add_movies():
        save_movies()

    # display trailer webpage
    display_trailer_webpage()


if __name__ == "__main__":
	main()
