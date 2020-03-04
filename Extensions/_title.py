from Extension import Extension
from threading import Thread
from re import findall
from mechanize import Browser
from urllib import quote_plus

class Define(Extension, Thread):
	
	def __init__(self, com):
		Extension.__init__(self, com)
		Thread.__init__(self)



	def run(self):
		try:
			url = self.com["message"]
			url = url.replace(" ", "+")
			br  = Browser()
			br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
			br.set_handle_robots(False)
			br.set_handle_redirect(True)
			br.open(url)
			self.SendToChannel(self.com["recipient"], br.title())
		except Exception, e:
			print e


