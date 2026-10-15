from data__displayer import DataDisplay

# Run through a series of commands to test the application
class HeadlessTest:
	def __init__(self, data_display : DataDisplay, user = None, session=None, session_manager=None):
		print(f"\n-- Headless Test --\n\nPresent :---:\n\n\tData Display: {data_display is not None}\n\tUser: {user is not None}\n\tSession: {session is not None}\n\tSession Manager: {session_manager is not None}\n\nTests   :---:\n")

		if session_manager is not None:
			print(session_manager.join_or_create_session("Test Session 1"))
			print(session_manager.join_or_create_session("Test Session 2"))
			print(session_manager.get_remote_sessions())
			print(session_manager.sessions[0].new_dataset("Test Dataset"))
			print(session_manager.sessions[0].add_datasource("test_data/test_data_a.csv", "Test Dataset"))
			print(session_manager.sessions[0].compile_dataset("Test Dataset"))
			print(session_manager.sessions[0].add_datasource("test_data/test_data_b.csv", "Test Dataset"))
			print(session_manager.sessions[0].compile_dataset("Test Dataset"))
			data_display.generate_chart_line(session_manager.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")
			data_display.generate_chart_bar(session_manager.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")
			data_display.generate_chart_pie(session_manager.sessions[0].compile_dataset("Test Dataset"), "value", "key", "diff", "apple")
			print(session_manager.sessions[0].remove_datasource("test_data_b.csv", "Test Dataset"))
			print(session_manager.sessions[0].compile_dataset("Test Dataset"))
			print(session_manager.sessions[0].rename_dataset("Test Dataset", "New Name"))
			print(session_manager.sessions[0].compile_dataset("Test Dataset"))
			print(session_manager.sessions[0].compile_dataset("New Name"))
			print(session_manager.sessions[0].remove_dataset("Test Dataset"))

			if user is not None:
				print(session_manager.sessions[0].send_message(user, "Hello World"))
				print(session_manager.sessions[0].get_messages())
    
		if session is not None:
			print(session.new_dataset("Test Dataset"))
			print(session.add_datasource("test_data/test_data_a.csv", "Test Dataset"))
			print(session.compile_dataset("Test Dataset"))
			print(session.add_datasource("test_data/test_data_b.csv", "Test Dataset"))
			print(session.compile_dataset("Test Dataset"))
			data_display.generate_chart_line(session.compile_dataset("Test Dataset"), "key", "value", "diff")
			data_display.generate_chart_bar(session.compile_dataset("Test Dataset"), "key", "value", "diff")
			data_display.generate_chart_pie(session.compile_dataset("Test Dataset"), "value", "key", "diff", "apple")
			print(session.remove_datasource("test_data_b.csv", "Test Dataset"))
			print(session.compile_dataset("Test Dataset"))
			print(session.rename_dataset("Test Dataset", "New Name"))
			print(session.compile_dataset("Test Dataset"))
			print(session.compile_dataset("New Name"))
			print(session.remove_dataset("Test Dataset"))