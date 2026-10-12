# Manage users in the database
from pymongo import MongoClient
import config

class UserManager:
	def __init__(self):
		self.client = MongoClient(config.MONGO_URI)
		self.client.admin.command("ping")
  
	def get_collection(self, collection):
		return self.client[config.DB_NAME][collection]
	
	def find_user(self, username):
		return self.get_collection(config.USER_COLLECTION).find_one({"username": username})

	def create_user(self, username, hash):
		userdata = {"username": username, "hash": hash}
		self.get_collection(config.USER_COLLECTION).insert_one(userdata)
		return "User created successfully"