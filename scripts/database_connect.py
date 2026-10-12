#  Connects to the database and saves/loads data.
from pymongo import MongoClient
from session import Session
import config

class DatabaseConnection:
	def __init__(self):
		self.client = MongoClient(config.MONGO_URI)
		self.client.admin.command("ping")
   
	def get_collection(self, collection):
		return self.client[config.DB_NAME][collection]
   
	def push_data(self, session: Session):
		if not session:
			return "Invalid session"
  
		formatted_data = { "session": session.session_name, "datasets": session.files.internal_db }
  
		return self.get_collection(config.SESSION_COLLECTION).find_one_and_replace({"session": session.session_name}, formatted_data, upsert=True)

	def pull_data(self, session: Session):
		if not session:
			return "Invalid session"

		pulled_data = self.get_collection(config.SESSION_COLLECTION).find_one({"session": session.session_name})

		if not pulled_data:
			return "No corelating session in database"

		pulled_datasets = []
	
		for datasource in pulled_data['datasets']:
			if datasource['dataset'] not in pulled_datasets:
				pulled_datasets.append(datasource['dataset'])
	
		session.session_name = pulled_data['session']
		session.files.datasets = pulled_datasets
		session.files.internal_db = pulled_data['datasets']

		return "Session pulled successfully"