from Extension import Extension
from threading import Thread
from re import findall
import socket

def Host2Ip(message):
	host = message
	host = host.replace("http://", "")
	return socket.gethostbyname(host)


class Define(Extension, Thread):
	
	def __init__(self, com):
		Extension.__init__(self, com)
		Thread.__init__(self)



	def run(self):
		try:
			host = self.com["message"].split(" ", 1)[0]
			ip   = Host2Ip(host)
			self.SendToChannel(self.com["recipient"], ip)
		except Exception, e:
			print e




	


