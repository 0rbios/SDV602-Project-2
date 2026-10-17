# Run through a series of commands to test the application
class HeadlessTest:
	def __init__(self, app, verbose : bool = False):
		print(f"\n-- Headless Test --")
  
		if verbose:
			print(f"\nPresent :---:\n\n\tData Display: {app.data_display is not None}\n\tUser: {app.user is not None}\n\tSession: {app.session is not None}\n\tSession Manager: {app.sm is not None}\n\nTests   :---:")

		if app.sm is not None:
			print(f"\nJoining a test session - ")
			if verbose:
				print(f"Function: SessionManager.join_or_create_session")
			print(app.sm.join_or_create_session("Test Session 1"))
   
			print(f"\nJoining another test session - ")
			if verbose:
				print(f"Function: SessionManager.join_or_create_session")
			print(app.sm.join_or_create_session("Test Session 2"))
   
			print(f"\nList both active sessions - ")
			if verbose:
				print(f"Function: SessionManager.get_remote_sessions")
			print(app.sm.get_remote_sessions())
   
			print(f"\nCreate a new dataset - ")
			if verbose:
				print(f"Function: Session.new_dataset")
			print(app.sm.sessions[0].new_dataset("Test Dataset"))
   
			print(f"\nAdd the first test datasource to the dataset - ")
			if verbose:
				print(f"Function: Session.add_datasource")
			print(app.sm.sessions[0].add_datasource("test_data/test_data_a.csv", "Test Dataset"))
   
			print(f"\nCompile with the single datasource - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.sm.sessions[0].compile_dataset("Test Dataset"))

			print(f"\nAdd the second test datasource to the dataset - ")
			if verbose:
				print(f"Function: Session.add_datasource")
			print(app.sm.sessions[0].add_datasource("test_data/test_data_b.csv", "Test Dataset"))

			print(f"\nCompile with both datasources - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.sm.sessions[0].compile_dataset("Test Dataset"))

			print(f"\nGenerate a line graph from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_line")
			app.data_display.generate_chart_line(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")
   
			print(f"\nGenerate a bar graph from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_bar")
			app.data_display.generate_chart_bar(app.sm.sessions[0].compile_dataset("Test Dataset"), "key", "value", "diff")
   
			print(f"\nGenerate a pie chart from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_pie")
			app.data_display.generate_chart_pie(app.sm.sessions[0].compile_dataset("Test Dataset"), "value", "key", "diff", "apple")

			print(f"\nRemove the second datasource from the test dataset - ")
			if verbose:
				print(f"Function: Session.remove_datasource")
			print(app.sm.sessions[0].remove_datasource("test_data_b.csv", "Test Dataset"))

			print(f"\nCompile the test dataset without the second datasource - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.sm.sessions[0].compile_dataset("Test Dataset"))

			print(f"\nRename the test dataset - ")
			if verbose:
				print(f"Function: Session.rename_dataset")
			print(app.sm.sessions[0].rename_dataset("Test Dataset", "New Name"))

			print(f"\nFail to compile the old dataset name - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.sm.sessions[0].compile_dataset("Test Dataset"))

			print(f"\nCompile the new dataset name - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.sm.sessions[0].compile_dataset("New Name"))

			print(f"\nCompletely remove the test dataset - ")
			if verbose:
				print(f"Function: Session.remove_dataset")
			print(app.sm.sessions[0].remove_dataset("New Name"))

			if app.user is not None:
				print(f"\nSend a message to the database - ")
				if verbose:
					print(f"Function: Session.send_message")
				print(app.sm.sessions[0].send_message(app.user, "Hello World"))

				print(f"\nReturn the session's chat log - ")
				if verbose:
					print(f"Function: Session.get_messages")
				print(app.sm.sessions[0].get_messages())
    
		if app.session is not None:
			print(f"\nCreate a new dataset - ")
			if verbose:
				print(f"Function: Session.new_dataset")
			print(app.session.new_dataset("Test Dataset"))

			print(f"\nAdd the first test datasource to the dataset - ")
			if verbose:
				print(f"Function: Session.add_datasource")
			print(app.session.add_datasource("test_data/test_data_a.csv", "Test Dataset"))

			print(f"\nCompile with the single datasource - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.session.compile_dataset("Test Dataset"))

			print(f"\nAdd the second test datasource to the dataset - ")
			if verbose:
				print(f"Function: Session.add_datasource")
			print(app.session.add_datasource("test_data/test_data_b.csv", "Test Dataset"))

			print(f"\nCompile with both datasources - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.session.compile_dataset("Test Dataset"))

			print(f"\nGenerate a line graph from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_line")
			app.data_display.generate_chart_line(app.session.compile_dataset("Test Dataset"), "key", "value", "diff")

			print(f"\nGenerate a bar graph from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_bar")
			app.data_display.generate_chart_bar(app.session.compile_dataset("Test Dataset"), "key", "value", "diff")

			print(f"\nGenerate a pie chart from the test dataset - ")
			if verbose:
				print(f"Function: DataDisplay.generate_chart_pie")
			app.data_display.generate_chart_pie(app.session.compile_dataset("Test Dataset"), "value", "key", "diff", "apple")

			print(f"\nRemove the second datasource from the test dataset - ")
			if verbose:
				print(f"Function: Session.remove_datasource")
			print(app.session.remove_datasource("test_data_b.csv", "Test Dataset"))

			print(f"\nCompile the test dataset without the second datasource - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.session.compile_dataset("Test Dataset"))

			print(f"\nRename the test dataset - ")
			if verbose:
				print(f"Function: Session.rename_dataset")
			print(app.session.rename_dataset("Test Dataset", "New Name"))

			print(f"\nFail to compile the old dataset name - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.session.compile_dataset("Test Dataset"))

			print(f"\nCompile the new dataset name - ")
			if verbose:
				print(f"Function: Session.compile_dataset")
			print(app.session.compile_dataset("New Name"))

			print(f"\nCompletely remove the test dataset - ")
			if verbose:
				print(f"Function: Session.remove_dataset")
			print(app.session.remove_dataset("New Name"))
