from GetExtensions import GetExtensions


def GetTupple(Text):
	#No need to explain
	key, value = Text.split(" ", 1)
	while value.endswith('\n') or value.endswith('\r'):
		value  = value[:-1]
	return key, value 

def GetConfigs(InputFile):
	Dictionnary 						= dict(GetTupple(i) for i in open(InputFile).readlines()) #Creating a dic with the configs
	if Dictionnary["debug"] == "True":
		Dictionnary["debug"] = True
        else:
                Dictionnary["debug"] = False
	Dictionnary["functions"]			= GetExtensions(Dictionnary["char"]) #Basically the Extensions/Plugins
	return Dictionnary
