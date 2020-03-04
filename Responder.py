class callFunction(object):
	def __init__(self, response, function):
		self.response = response
		self.function = function

	def __call__(self, socket, recipient):
		if self.response != None or self.response:
			self.function(self.response, socket, recipient)
		else:
			self.function(socket, recipient)

def ReplyFunction(response, socket, recipient):
	socket.send('PRIVMSG {0} :{1}\r\n'.format(recipient, response))


def createDic(listofkeys, value):
	dic = {}
	for i in listofkeys:
		dic[i] = value
	return dic


Dictionnary = [
createDic(["backtrack"] , callFunction("OMG l33t hax0r.", ReplyFunction)),
createDic(["python", "c++"] ,callFunction("The best programming language ever.", ReplyFunction))
]






def GetResponse(message):
	ListOfReplies = []
	for word in message.split():
		i  = 0
		while i < len(Dictionnary):
			if word in Dictionnary[i]:
				ListOfReplies.append(Dictionnary[i][word])
			i+=1
	return ListOfReplies