import sys
from Classes.digikey import digikey

#    ____  _       _ __ __              ______     __       __  
#   / __ \(_)___ _(_) //_/__  __  __   / ____/__  / /______/ /_ 
#  / / / / / __ `/ / ,< / _ \/ / / /  / /_  / _ \/ __/ ___/ __ \
# / /_/ / / /_/ / / /| /  __/ /_/ /  / __/ /  __/ /_/ /__/ / / /
#/_____/_/\__, /_/_/ |_\___/\__, /  /_/    \___/\__/\___/_/ /_/ 
#        /____/            /____/                               
#
#   Simple DigiKey fetch class
#   URL     : http://sasakaranovic.com/projects/digikey-fetch-tool/
#   Author  : Sasa Karanovic
#   Version : 0.1
#

#Initialize DigiKey fetch class
dk = digikey()


#Ask user to provide URL for the first time
dk.AskForURL()

#Main Loop
while(1):
    dk.DisplayMenuOptions() 
  

