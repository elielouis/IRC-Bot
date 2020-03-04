from Extension import Extension
from threading import Thread
from mechanize import Browser

def isUp(host):
	br   = Browser()
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.open("http://doj.me/?url={0}".format(host))
	if "UP" in br.response().read():
		return True
	else:
		return False


class isTheSiteDown(Extension, Thread):
	
	def __init__(self, com):
		Extension.__init__(self, com)
		Thread.__init__(self)



	def run(self):
		try:
			host = self.com["message"].split(" ", 1)[0]
			host = host.replace("http://", "")
			condition = isUp(host)
			if condition:
				message = "It's just you! It's up here!"
			else:
				message = "It's down for everyone"
			self.SendToChannel(self.com["recipient"], message)
		except Exception, e:
			print e


	




