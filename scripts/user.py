# The user who is logged in to the application.
import bcrypt
from user_manager import UserManager

class User:
	def __init__(self):
		self.username = None
		self.db = UserManager()

	def get_hash(self, password):
		bytes = password.encode('utf-8')

		salt = bcrypt.gensalt()
		hash = bcrypt.hashpw(bytes, salt)
  
		return hash

	def register_user(self, username, password):
		existing_user_check = self.db.find_user(username)
  
		if existing_user_check:
			return "User already exists"

		self.username = username
		return self.db.create_user(username, self.get_hash(password))

	def log_in_user(self, username, password):
		found_user = self.db.find_user(username)

		if not found_user:
			return "Login Failed"

		if bcrypt.checkpw(password.encode('utf-8'), found_user["hash"]):
			self.username = found_user["username"]
			return "Login Success"
		else:
			return "Login Failed"