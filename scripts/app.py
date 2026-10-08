# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from file_manager import FileManager

if __name__ == "__main__":
	fm = FileManager()
 
	print(fm.create_dataset("test"))
 
	print(fm.load_data_source("C:/Users/dyfry/Desktop/Don't Look.txt", "test"))
 
	print(fm.compile_dataset("test"))
 
	print(fm.remove_data_source("Don't Look.txt", "test"))
 
	print(fm.compile_dataset("test"))

	print(fm.remove_dataset("test"))