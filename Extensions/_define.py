from Extension import Extension
from threading import Thread
from re import findall
from mechanize import Browser

class Define(Extension, Thread):
	
	def __init__(self, com):
		Extension.__init__(self, com)
		Thread.__init__(self)



	def run(self):
		try:
			word = self.com["message"].split(' ', 1)[0]
			br   = Browser()
			br.set_handle_robots(False)
			br.open('http://api.duckduckgo.com/?q=define+{0}&format=json&pretty=1'.format(word))
			regex  =  """"AbstractText" : "(.*)["]{1}"""
			definition = findall(regex,  br.response().read())[0]
			self.SendToChannel(self.com["recipient"], definition)
		except Exception, e:
			print e


