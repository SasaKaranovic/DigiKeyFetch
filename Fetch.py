import os
import sys
import clipboard
from Classes.digikey import digikey
from Classes.globalhotkeys import GlobalHotKeys

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
#   Version : 0.2
#
#	Usage	: Run Fetch.py script. When prompted, enter valid DigiKey part URL
#			  Script will retrieve part information and then you can use shortcuts to copy
#			  part information to clipboard
#


#Initialize DigiKey fetch class
dk = digikey()


#define HotKeys to use

@GlobalHotKeys.register(GlobalHotKeys.VK_1, GlobalHotKeys.MOD_ALT)
def CopyManufacturer():
    clipboard.copy(dk.Manufacturer)
    print "Manufacturer info copied to clipboard."

@GlobalHotKeys.register(GlobalHotKeys.VK_2, GlobalHotKeys.MOD_ALT)
def CopyManufacturerPN():
    clipboard.copy(dk.ManufacturerPN)
    print "ManufacturerPN info copied to clipboard."

@GlobalHotKeys.register(GlobalHotKeys.VK_3, GlobalHotKeys.MOD_ALT)
def CopyDistributor():
    clipboard.copy("DigiKey")
    print "Distributor info copied to clipboard."

@GlobalHotKeys.register(GlobalHotKeys.VK_4, GlobalHotKeys.MOD_ALT)
def CopyDistributorPN():
    clipboard.copy(dk.DigiKeyPN)
    print "DigiKeyPN info copied to clipboard."

@GlobalHotKeys.register(GlobalHotKeys.VK_5, GlobalHotKeys.MOD_ALT)
def CopyDescription():
    clipboard.copy(dk.Description)
    print "Description info copied to clipboard."


@GlobalHotKeys.register(GlobalHotKeys.VK_0, GlobalHotKeys.MOD_ALT)
def ReStart():
    dk.AskForURL()

# ctrl+q will exit script
GlobalHotKeys.register(GlobalHotKeys.VK_Q, GlobalHotKeys.MOD_CTRL, False)


#Ask user to provide URL for the first time
dk.AskForURL()

#Main Loop
GlobalHotKeys.listen()

    
  

