'''
What it does:
	Goes in the folder Extensions
	Passes in all the modules that starts with _ one by one
	Passes in all the data of the module
	Adds a list to the dictionnary with as key the name of the module.replace("_", the character from the settings)
	Looks if any of the data is a Class that is a child of The Extension mother class (Here called ExtensionType)
	Appends them to the list of the dictionnary[module]
To execute them later you would have to write:
	.modulename args
'''
import types
import sys
import types
__import__('Extensions')
Extensions = sys.modules['Extensions']
ExtensionType  = Extensions.Extension.Extension 

ignoreList = ['__builtins__',
'__doc__',
'__file__',
'__name__',
'__package__',
'__path__',
'__all__',
'Extension',
'Thread']

def GetExtensions(char):
	MyExtensions 			      =  {}
	Modules 			          =  [x for x in dir(Extensions) if x.startswith("_")]  #Get the module names
	for i in ignoreList:
		if i in Modules:
			Modules.remove(i)


	
	for Module in Modules:
		ModuleObject			  = getattr(Extensions, Module)
		Functions 			      = dir(ModuleObject) #Get the functions of the module
		for i in ignoreList:
			if i in Functions:
				Functions.remove(i)
		NewList 				  = []
		for i in Functions:
			i 					  = getattr(ModuleObject, i)
			if str(type(i)) == "<type 'type'>":
				if issubclass(i, ExtensionType):
					NewList.append(i)
		Functions                 = NewList
		ModuleName				  = Module.replace('_', char)
		MyExtensions[ModuleName]  = []
		for Function in Functions:
			MyExtensions[ModuleName].append(Function)

	return MyExtensions