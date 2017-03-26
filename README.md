# Movie Trailer Website

In this project, I wrote a Python class to hold movie objects and used this class to generate a website to display favorite movies.

Specifically, I created a Python movie class in module `media.py`. Then I employed this class to create instances of a few of my favorite movies. We were supplied with a Python module called `fresh_tomatoes.py` to generate a website to display these movies. Finally, I created a list of these movie objects and passed them to the `open_movies_page` function to dynamically generate an HTML file for the website.

The resulting website displays the poster art and title of each featured movie. When you click on any poster, the YouTube movie trailer for that movie will appear and begin playing. Clicking on the trailer will stop the playback and close the modal window.

### How to run this website

To run this website, you will need to download 3 files:
* `fresh_tomatoes.py` - Contains the server-side code to create and launch the  website.
* `media.py` - Contains the class definition for Movie objects.
* `entertainment_center.py` - Contains the main script to create movie objects and calls the function which generates and opens the movies page.

Once all 3 files are downloaded, execute `entertainment_center.py` in your Python IDE. This will launch your web browser and display my movie page.

#### Attributions

This project is part of Udacity's Full Stack Web Developer nanodegree.

All movie poster art URLs were found on [www.wikipedia.org](www.wikipedia.org).
All movie trailer URLs were taken from [www.youtube.com](www.youtube.com).
