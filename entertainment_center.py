# Script to instantiate a list of favorite movie objects and create a web
# page to display them.
# Dependencies: fresh_tomatoes.py, media.py
import fresh_tomatoes
import media


def display_movies():
    """ display_movies() creates a list of favorite movie objects and calls
    open_movies_page function to create a web page displaying them.
    """
    # create movie instances for some of my favorite movies
    lord_of_the_rings = media.Movie("The Lord of the Rings",
                                    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=KOQSQaGgJxs"  # NOQA
                                    )
    harry_potter = media.Movie("Harry Potter (series)",
                               "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=MqUkT32rYac"
                               )
    princess_bride = media.Movie("The Princess Bride",
                                 "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=O3CIXEAjcc8"
                                 )
    beauty_beast = media.Movie("Beauty and the Beast",
                               "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=e3Nl_TCQXuw"
                               )
    finding_nemo = media.Movie("Finding Nemo",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=SPHfeNgogVs"
                               )
    shaun_the_sheep = media.Movie("Shaun the Sheep Movie",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Shaun_the_Sheep_MoviePoster.jpg/220px-Shaun_the_Sheep_MoviePoster.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=tQvwiOWpj7o"
                                  )                           
    # store movies in a list
    movies = [lord_of_the_rings, harry_potter, princess_bride, finding_nemo, beauty_beast, shaun_the_sheep]
    # build the website to display these movies
    fresh_tomatoes.open_movies_page(movies)


display_movies()

