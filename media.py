import webbrowser


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, director, budget, box_office, running_time,
                 rating, release_date, genre):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_director = director
        self.movie_genre = genre
        self.budget = budget
        self.box_office = box_office
        self.running_time = running_time
        self.rating = rating
        self.release_date = release_date

    # Opens a webpage to the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # Displays the storyline of the movie
    def show_storyline(self):
    	return self.storyline






