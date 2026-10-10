# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from file_manager import FileManager
from data__displayer import DataDisplay

if __name__ == "__main__":
	fm = FileManager()
	dd = DataDisplay()
 
	print(fm.create_dataset("test"))
 
	print(fm.load_data_source("C:/Users/dyfry/Downloads/bd-natural-increase-2010-2014.csv", "test"))
 
	# dd.generate_chart_line(fm.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")
 
	print(fm.load_data_source("C:/Users/dyfry/Downloads/bd-natural-increase-2015-2019.csv", "test"))
  
	# dd.generate_chart_line(fm.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")

	# dd.generate_chart_pie(fm.compile_dataset("test"), "Count", "Period", "Births_Deaths_or_Natural_Increase", "Natural_Increase")
   
	dd.generate_chart_bar(fm.compile_dataset("test"),  "Period", "Count", "Births_Deaths_or_Natural_Increase")

	# print(fm.remove_data_source("bd-natural-increase-2010-2014.csv", "test"))
 
	# print(fm.compile_dataset("test"))

	# print(fm.remove_dataset("test"))