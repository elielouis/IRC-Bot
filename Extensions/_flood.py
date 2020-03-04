from Extension import Extension
from threading import Thread

class msgFlood(Extension, Thread):
	
	def __init__(self, com):
		Thread.__init__(self)
		Extension.__init__(self, com)


	def run(self):
		if self.com["super"]:
			try:
				channel, nTime ,message		= self.com["message"].split(" ", 2)
				nTime						= int(nTime)
				for i in xrange(nTime):
					self.SendToChannel(channel, message)
			except Exception, e:
				print e

