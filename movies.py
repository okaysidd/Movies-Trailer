import webbrowser


class Movies():
    """Used to instantiate the movies object with movies details

    Attributes:
        movie_title(str): used to store the title of the movie (usually a few words)
        movie_storyline(str): used to store the storyline (usually a few sentences)
        poster_image(str): used to store the link to the poster of the movie (url)
        trailer_youtube(str): used to store the YouTube link to the trailer to the movie (YouTube url)
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        instantiate the self varibles that will be used to create the movies object
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
