# A session being hosted with its own chat, data and users.
from file_manager import FileManager
from database_connect import DatabaseConnection

class Session:
	def __init__(self, name, remote = False):
		self.session_name = name
		self._files = FileManager()
		
		self.db = None
  
		if remote == True:
			self.db = DatabaseConnection()
			self.db.pull_data(self)
   
	def new_dataset(self, name):
		self._files.create_dataset(name)

		if self.db:
			self.db.push_data(self)

		return f"Dataset '{name}' successfully created"
   
	def add_datasource(self, file, dataset):
		self._files.load_data_source(file, dataset)
  
		if self.db:
			self.db.push_data(self)

		return f"Datasource '{file}' successfully added to '{dataset}'"
  
	def remove_dataset(self, name):
		self._files.remove_dataset(name)
  
		if self.db:
			self.db.push_data(self)

		return f"Dataset '{name}' successfully removed"

	def remove_datasource(self, file, dataset):
		self._files.remove_data_source(file, dataset)
  
		if self.db:
			self.db.push_data(self)

		return f"Datasource '{file}' successfully removed from '{dataset}'"

	def rename_dataset(self, old_name, new_name):
		self._files.rename_dataset(old_name, new_name)
  
		if self.db:
			self.db.push_data(self)
  
		return f"Datasource '{old_name}' successfully renamed to '{new_name}'"

	def compile_dataset(self, dataset):
		if self.db:
			self.db.pull_data(self)
    
		return self._files.compile_dataset(dataset)