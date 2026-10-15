# The entrypoint into the application, parses any CLI arguments, establishes starting values and runs the application.
from session import Session
from session_manager import SessionManager
from data__displayer import DataDisplay
from user import User
from headless import HeadlessTest

REMOTE = True
HEADLESS = True

if __name__ == "__main__":  
	sm = None
	user = None
	session = None
   
	if REMOTE:
		sm = SessionManager()
		user = User()
	else:
		session = Session("Local Session", remote=False)
  
	data_display = DataDisplay()
 
	if HEADLESS:
		HeadlessTest(data_display=data_display, user=user, session=session, session_manager=sm)