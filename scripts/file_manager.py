# Loads data from files and manages them.
import os
class FileManager:
	def __init__(self):
		self.internal_db = []
		self.datasets = []

	def compile_dataset(self, dataset):
		if dataset not in self.datasets:
			return "Invalid tag"

		compiled_result = []

		for file in self.internal_db:
			if file["dataset"] == dataset:
				compiled_result.append(file["data"])
    
		return compiled_result

	def load_data_source(self, filepath, dataset):
		if dataset not in self.datasets:
			return "Invalid dataset"
    
		try:
			with open(filepath) as File:
				filename = os.path.basename(filepath)
				data = File.readlines()
				data_packet = {"filename": filename, "dataset": dataset, "data": data}
				self.internal_db.append(data_packet)
				return "File loaded successfully"
   
		except:
			return "File not found "
 
	def create_dataset(self, dataset):
		if dataset in self.datasets:
			return "Dataset already exists"

		self.datasets.append(dataset)
		return "Dataset created successfully"
 
	def remove_dataset(self, dataset):
		if dataset not in self.datasets:
			return "Dataset not found"

		self.internal_db = [file for file in self.internal_db if file["dataset"] != dataset]
		self.datasets.remove(dataset)

		return "Dataset removed successfully"
 
	def rename_dataset(self, dataset, new_name):
		if dataset not in self.datasets:
			return "Dataset not found"

		if new_name in self.datasets:
			return "Dataset already exists"

		self.datasets.remove(dataset)
		self.datasets.append(new_name)

		return "Dataset updated correctly"
 
	# Remove a data source from the internal db
	def remove_data_source(self, filename, dataset):
		if dataset not in self.datasets:
			return "Dataset not found"
		
		for datasource in self.internal_db:
			if datasource["dataset"] == dataset and datasource["filename"] == filename:
				self.internal_db.remove(datasource)

		return "Datasource removed successfully"