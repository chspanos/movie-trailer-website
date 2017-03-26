class Movie():
    """ This class defines a Movie object.

    Attributes:
        title -- specifies the movie's title
        poster_image_url -- specifies a URL for the movie poster image
        trailer_youtube_url -- specifies the YouTube URL for the trailer
    """

    def __init__(self, title, poster_url, trailer_url):
        """ Constructor for the movie object """
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
