# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from data__displayer import DataDisplay
from database_connect import DatabaseConnection

if __name__ == "__main__":
	session = Session("Test Session")
	dd = DataDisplay()
	db = DatabaseConnection()
 
	print(db.pull_data(session))
 
	# print(session.files.create_dataset("test"))
 
	# print(session.files.load_data_source("C:/Users/dyfry/Downloads/bd-natural-increase-2010-2014.csv", "test"))
 
	# dd.generate_chart_line(session.files.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")
 
	# print(session.files.load_data_source("C:/Users/dyfry/Downloads/bd-natural-increase-2015-2019.csv", "test"))
  
	# dd.generate_chart_line(session.files.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")

	# dd.generate_chart_pie(session.files.compile_dataset("test"), "Count", "Period", "Births_Deaths_or_Natural_Increase", "Natural_Increase")
   
	# dd.generate_chart_bar(session.files.compile_dataset("test"),  "Period", "Count", "Births_Deaths_or_Natural_Increase")

	print(session.files.remove_data_source("bd-natural-increase-2010-2014.csv", "test"))
 
	# print(session.files.compile_dataset("test"))

	# print(session.files.remove_dataset("test"))

	print(db.push_data(session))