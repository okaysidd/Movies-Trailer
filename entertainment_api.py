import tmdbsimple as tmdb
import urllib
import fresh_tomatoes as ft
import json
import movies
import webbrowser

tmdb.API_KEY = '9ee394eab0a844afcd7dbf8af77bded5'

with open('movies_details.json','r') as file:
    json_movies_data = json.load(file)

# to save all movie titles to inform user if adding some movie twice
movie_titles = []
for i in range(len(json_movies_data['movies'])):
	movie_titles.append(json_movies_data['movies'][i]['movie_title'])

#---------------------------------------------------------------
# displaying all the current movies' details in the json file
def show_movies():
    print('The movies website currently has {} movies. The following:\n'.format(len(json_movies_data['movies'])))
    for i in range(len(json_movies_data['movies'])):
        print('{}. {}'.format(i+1, json_movies_data['movies'][i]['movie_title']))


#---------------------------------------------------------------
# let user add new movies if needed
def search_for_movie():

	while True:
		movie_name = input('\nWhich movie should we add to the trailers webpage?\n')
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
			print('Is this the movie you meant? {} - release date- {}'.format(movies_list[0]['title'], movies_list[0]['release_date']))
			movie_picked = input('Y/N  ').lower()
			if movie_picked == 'yes' or movie_picked == 'yus' or movie_picked == 'y': # check for 'no' response as well
				movie_picked = movies_list[0]['id']
				return movie_picked

		# if search returned more than one result for the movie name
		number=1
		print('\nWhich movie did you mean?')
		print()
		for s in movies_list[:3]:
			print('{}. {} -- release in {}'.format(str(number), s['title'], s['release_date']))
			number+=1
		print()
		print('{}. None of these'.format(str(number)))
		movie_choice = input('Enter a number..  ')

		if movie_choice=='4':
			continue
		elif movie_choice=='':
			print('That\'s an invalid input.')
			continue
		elif movie_choice in '123' and int(movie_choice) <= number:
			movie_picked = movies_list[int(movie_choice)-1]
			return movie_picked
		else:
			print('That\'s an invalid input.')
			continue

#---------------------------------------------------------------
# get the youtube link of the movie selected from the api link
def get_youtube_link(movie_picked):

	# the api link to get the movie data
	link = 'https://api.themoviedb.org/3/movie/'+ movie_picked + '/videos?api_key=9ee394eab0a844afcd7dbf8af77bded5&language=en-US'
	source = urllib.request.urlopen(link)

	# getting the movie data in json format from the http request format that the above api returns
	data = source.read().decode("utf-8")
	jmovie_data = json.loads(data)
	youtube_link_key = jmovie_data["results"][0]['key']
	youtube_link = 'https://www.youtube.com/watch?v=' + youtube_link_key
	return youtube_link

#---------------------------------------------------------------
# choice to save these movies permanently in the json file
def save_movies():
    save_movies = input('Save these movies permanently? Y/N  ')
    if save_movies=='yes' or save_movies=='yus' or save_movies=='y':
        with open('movies_details.json', 'w') as file:
            json.dump(json_movies_data, file)


#---------------------------------------------------------------
# creating Movies() objects of all the movies present in the movies_details.json file, then displaying
def display_trailer_webpage():
	movies_list=[]
	for i in range(len(json_movies_data['movies'])):
	    name = json_movies_data['movies'][i]['movie_title']
	    # formatting the movie title so that object name is always without spaces, and also makes sense
	    #movie_title = ('_').join(name.split())
	    movie_title = name
	    movie_storyline = json_movies_data['movies'][i]['movie_storyline']
	    poster_image = json_movies_data['movies'][i]['poster_image']
	    trailer_youtube = json_movies_data['movies'][i]['trailer_youtube']
	    # adding object each time to the list of movie objects
	    movies_list.append(movies.Movies(movie_title, movie_storyline, poster_image, trailer_youtube))

    # using fresh_tomatoes.py file to finally open the webpage with the movie object items
	ft.open_movies_page(movies_list)


#---------------------------------------------------------------
# main method
def main():

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
				ch = input('A movie with the same name already exists. Continue to add? Y/N  ').lower()
				if ch!='yes' and ch!='yus' and ch!='y':
					continue

			movie_storyline = movie_picked['overview']
			poster_image = 'https://image.tmdb.org/t/p/original' + str(movie_picked['poster_path'])
			# webbrowser.open(movie_poster)

			# getting the youtube link and the storyline from the json response of the api
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


if __name__=='__main__':
	main()