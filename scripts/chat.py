# Manages messages.
from message import Message

class Chat:
	def __init__(self):
		self.messages = []
   
   
	def send_message(self, sender, contents):
		"""Adds a new message object to the internal message list."""
		self.messages.append(Message(sender.username, contents))
  
  
	def get_messages(self):
		"""Return all of the internal messages formatted as a chat string."""
		output = ""
  
		for message in self.messages:
			if self.messages.index(message) != 0:
				output += f"\n"
   
			output += f"{message.sender}: {message.contents}"
  
		return output