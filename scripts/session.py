# A session being hosted with its own chat, data and users.
from file_manager import FileManager

class Session:
	def __init__(self, name):
		self.session_name = name
		self.files = FileManager()