# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from data__displayer import DataDisplay
from user import User

if __name__ == "__main__":
	user1 = User()
	user2 = User()
	session = Session("Test Session", remote=True)
	dd = DataDisplay()
	
	user1.register_user("Test User", "Password123")
	user2.register_user("Other User", "Second Password")
 
	session.send_message(user1, "This is a test")

	session.send_message(user2, "And another message")
 
	session.send_message(user1, "Hello World")
 
	print(session.get_messages())
 
	# print(session.new_dataset("test"))
 
	# print(session.add_datasource("C:/Users/dyfry/Downloads/bd-natural-increase-2010-2014.csv", "test"))
	# print(session.add_datasource("C:/Users/dyfry/Downloads/bd-natural-increase-2015-2019.csv", "test"))
 
	# dd.generate_chart_line(session.compile_dataset("test"), "Period", "Count", "Births_Deaths_or_Natural_Increase")
	# dd.generate_chart_pie(session.compile_dataset("test"), "Count", "Period", "Births_Deaths_or_Natural_Increase", "Natural_Increase")
	# dd.generate_chart_bar(session.compile_dataset("test"),  "Period", "Count", "Births_Deaths_or_Natural_Increase")