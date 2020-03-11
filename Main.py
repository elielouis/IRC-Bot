from IRC import Run # Importing the Runner
from Configs import GetConfigs # Importing the settings getter

def main():
	var = """|       \            |  \    |  \              |  \      
| $$$$$$$\  ______  _| $$_  _| $$_     ______  | $$   __ 
| $$__/ $$ /      \|   $$ \|   $$ \   /      \ | $$  /  \\
| $$    $$|  $$$$$$\\\\$$$$$$ \$$$$$$  |  $$$$$$\| $$_/  $$
| $$$$$$$\| $$  | $$ | $$ __ | $$ __ | $$  | $$| $$   $$ 
| $$__/ $$| $$__/ $$ | $$|  \| $$|  \| $$__/ $$| $$$$$$\ 
| $$    $$ \$$    $$  \$$  $$ \$$  $$ \$$    $$| $$  \$$\\
 \$$$$$$$   \$$$$$$    \$$$$   \$$$$   \$$$$$$  \$$   \$$

        version : {0}                  Author:     {1}:{2}

        """.format(__version__, __author__, __email__)
        print var
        Settings             = GetConfigs("configs.txt") #Get the settings
        Run(Settings).start() # Run the bot

if __name__ == '__main__':
	main()
