import webbrowser


# creating a class Movie
class Movie():
    def __init__(self, movie_title, story_line, movie_poster, trailer_url):
        # intializing __init__ attributes
        self.title = movie_title
        self.moviestory = story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_url
