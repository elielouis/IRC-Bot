from Extension import Extension
from threading import Thread
class msgChannel(Extension, Thread):
	
	def __init__(self, com):
		Extension.__init__(self, com)
		Thread.__init__(self)



	def run(self):
		try:
			receiver, message = self.com["message"].split(' ', 1)
			self.SendToChannel(receiver, message)
		except Exception, e:
			print e

