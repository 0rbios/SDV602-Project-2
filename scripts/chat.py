# Manages messages.
from message import Message

class Chat:
	def __init__(self):
		self.messages = []
   
	def send_message(self, sender, contents):
		self.messages.append(Message(sender.username, contents))
  
	def get_messages(self):
		output = ""
  
		for message in self.messages:
			if self.messages.index(message) != 0:
				output += f"\n"
   
			output += f"{message.sender}: {message.contents}"
  
		return output