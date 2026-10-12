# A message sent by a user in a chat in a session.
class Message:
	def __init__(self, sender, contents):
		self.sender = sender
		self.contents = contents