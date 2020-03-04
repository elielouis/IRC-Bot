from Extension import Extension
from threading import Thread

class msgSend(Extension, Thread):
	
	def __init__(self, com):
		Thread.__init__(self)
		Extension.__init__(self, com)


	def run(self):
		if self.com["super"]:
			try:
				self.Send('{0}\r\n'.format(self.com["message"]))
			except Exception, e:
				print e


