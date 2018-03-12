# jmiu CS4308

class Book:

	import json

	def __init__(self, _author, _title, _pages) :
		self.author = _author
		self.title = _title
		self.pages = _pages

	def get_json(self) :
		return {'author' : self.author, 'title' : self.title, 'pages' : self.pages}

	def set_author(self, _author) :
		self.author = _author

	def set_title(self, _title) :
		self.title = _title

	def set_pages(self, _pages) :
		self.pages = _pages

