'''
This is the mother class
'''

class Extension():
	
	def __init__(self, com):
		self.com	 	 = com
		self.irc 		 = self.com["irc"]
		

	def Send(self, string):
		try:
			self.irc.send('{0}\r\n'.format(string).encode())
		except Exception ,e:
			pass
	
	def SendToChannel(self, channel, message):
		self.irc.send('PRIVMSG {0} :{1}\r\n'.format(channel, message))

