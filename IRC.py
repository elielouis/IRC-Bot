
from threading import Thread
from Responder import GetResponse
import socket
import time
import re
import types
import sys


class Server(object):
    def __init__(self, ip, port):
        self.host     =  ip
        self.port      = port

class Run(Thread):
    
    def __init__(self, configs):
        self.configs            = configs               # Configs , it is a dictionnary
        self.server             = Server(self.configs["host"], int(self.configs["port"]))
        self.irc                = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.loggedin           = False
        self.connected          = False
        self.pat = re.compile(":([^!]+)!(\S+)\s+(\S+)\s+:?(\S+)\s*(?:[:+-]+(.*))?(?:[:+-]+(.*))?") #Regular expression, didn't do it myself
        Thread.__init__(self)
        
    def initconfigs(self):
        #Initializin the configs
        self.debug              = self.configs["debug"]
        self.nick               = self.configs["nick"]
        self.channel            = self.configs["channel"]
        self.functions          = self.configs["functions"]
        self.configs["masters"] = self.configs["masters"].split(',')
        self.char               = self.configs["char"]
    
    def Action(self, command, data):
        #Doing an action
        if len(data.rsplit()) > 0:
            self.send("{0} {1}".format(command, data))
        else:
            self.send("{0}".format(command))

    def showOut(self, text):
        #Showing out
        if self.debug:
            print "Debug : {0}".format(text)

    def send(self, string):
        #Sending a message to the irc
        try:
            self.irc.send('{0}\r\n'.format(string).encode())
        except Exception as e:
            self.showOut(str(e))

    def connect(self):
        #Connecting (Not identifying yet)
        self.irc.connect((self.server.host, self.server.port))
        self.Action('NICK', self.nick)
        self.Action('USER', '{0} {1}'.format(self.nick, self.configs["user"]))
        self.showOut("Connected")
        self.connected = True


    def run(self):
        self.initconfigs()
        self.connect()
        self.mainLoop()


    def mainLoop(self):
        while self.connected:
            data                 = self.irc.recv(1024)
            datas                = data.split("\r\n")
            for data in datas:
                if len(data.rsplit()) > 0:
                    if data.startswith("PING"): #Ping back
                        self.Action('PONG', data.split()[-1])
                        self.showOut('PONG {0}'.format(data.split()[-1]))

                    elif "IDENTIFY" in data and self.loggedin == False: 
                        #Identify and Join channel
                        self.Action('NickServ', 'IDENTIFY {0}'.format(self.configs['password']))
                        self.loggedin = True
                        time.sleep(3)
                        self.Action('JOIN', self.configs["channel"])

                    else:
                        self.showOut(data)
                        self.handleMsg(data)


    def handleMsg(self, data):
        reg = self.pat.match(data)
        if reg != None:
            try:
                g                   = reg.groups()
                com                 = dict(zip(['nick', 'user', 'action', 'recipient', 'message'],
                                     [item.rstrip() for item in g if item != None])) #Not done by me
                com["channel"]      = self.channel
                com["irc"]          = self.irc
                com['orig']         = data
                com["super"]        = com["nick"] in self.configs["masters"]
                user                = com['user'].split('@')
                com['user']         = user[0]
                com['uhost']        = user[1]
                if not com["recipient"].startswith("#"):
                    com["recipient"] = com["nick"] #just in case a user is talking to the bot, sometimes it has a problem..
                if com.has_key("message"):

                    response = GetResponse(com["message"])
                    if len(response) > 0:
                        for action in response:
                            action(com["irc"], com["recipient"])

                    if len(com["message"].split(" ")) < 2: #In case the message is just the command, without any parameter
                        com["command"] = com["message"]
                        if com["command"].startswith("{0}quit".format(self.char)):
                            if com['super']:
                                self.quit(com["message"])
                            
                        elif com["command"].startswith("{0}list".format(self.char)):
                            toSend = ''
                            for i in self.functions:
                                toSend += str(i).replace(self.char, "") + ", "
                            toSend = toSend[:-2]
                            self.Action("PRIVMSG", "{0} :{1}".format(com["recipient"], toSend))

                        elif com["command"].startswith("{0}masters".format(self.char)):
                            toSend = ''
                            for i in self.configs["masters"]:
                                toSend += i + ", "
                            toSend = toSend[:-2]
                            self.Action("PRIVMSG", "{0} :{1}".format(com["recipient"], toSend))

                    else:
                        com["command"], com["message"]      = com["message"].split(" ", 1)
                        if com["command"] == "{0}login".format(self.char):
                            if not com["nick"] in self.configs["masters"]:
                                if com["message"] == self.configs["passcode"]:
                                    self.configs["masters"].append(com["nick"]) #New user, basically a logging in

                    if com["command"] in self.functions: #If it's a command
                        Actions         = self.functions[com["command"]]
                        for action in Actions:
                            action(com).start() #Execute all it's functions.
            except:
                pass


    def quit(self, data):
        if  len(data.rsplit()) == 0:
            data = "Bye"
        self.Action("QUIT", data)

        self.connected        = False
        sys.exit(0)


