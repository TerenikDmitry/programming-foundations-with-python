import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, movie_image_url, movie_video_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.image_url = movie_image_url
		self.video_url = movie_video_url

	def show_trailer(self):
		webbrowser.open(self.video_url)
		