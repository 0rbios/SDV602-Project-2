# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from data__displayer import DataDisplay

if __name__ == "__main__":
	session = Session("Test Session", remote=True)
	dd = DataDisplay()
 
	# print(session.new_dataset("test"))
 
	# print(session.add_datasource("C:/Users/dyfry/Downloads/bd-natural-increase-2010-2014.csv", "test"))
 
	dd.generate_chart_line(session.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")
 
	# print(session.add_datasource("C:/Users/dyfry/Downloads/bd-natural-increase-2015-2019.csv", "test"))
  
	dd.generate_chart_line(session.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")

	dd.generate_chart_pie(session.compile_dataset("test"), "Count", "Period", "Births_Deaths_or_Natural_Increase", "Natural_Increase")
   
	dd.generate_chart_bar(session.compile_dataset("test"),  "Period", "Count", "Births_Deaths_or_Natural_Increase")

	# print(session.remove_datasource("bd-natural-increase-2010-2014.csv", "test"))
 
	# print(session.compile_dataset("test"))

	# print(session.remove_dataset("test"))