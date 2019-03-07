import os
import sys
import signal
import clipboard
import keyboard
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

# catch ctrl-c
def ctrl_c_handler(signal, frame):
    print("Goodbye!")
    exit()


def main():
    #Initialize DigiKey fetch class
    dk = digikey()


    #define HotKeys to use

    # Hotkey -> CTRL+1
    @GlobalHotKeys.register(GlobalHotKeys.VK_1, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturer():
        clipboard.copy("Manufacturer")
        keyboard.write("Manufacturer")
        print("'Manufacturer' info copied to clipboard.")

    # Hotkey -> CTRL+2
    @GlobalHotKeys.register(GlobalHotKeys.VK_2, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturer():
        clipboard.copy(dk.Manufacturer)
        keyboard.write(dk.Manufacturer)
        print("'%s' copied to clipboard." % dk.Manufacturer)

    # Hotkey -> CTRL+3
    @GlobalHotKeys.register(GlobalHotKeys.VK_3, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturerPN():
        clipboard.copy("Manufacturer Part Number")
        keyboard.write("Manufacturer Part Number")
        print("'Manufacturer Part Number' copied to clipboard.")

    # Hotkey -> CTRL+4
    @GlobalHotKeys.register(GlobalHotKeys.VK_4, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturerPN():
        clipboard.copy(dk.ManufacturerPN)
        keyboard.write(dk.ManufacturerPN)
        print("'%s' copied to clipboard." % dk.ManufacturerPN)

    # Hotkey -> CTRL+5
    @GlobalHotKeys.register(GlobalHotKeys.VK_5, GlobalHotKeys.MOD_CTRL)
    def CopyDistributor():
        clipboard.copy("Distributor")
        keyboard.write("Distributor")
        print("'Distributor' copied to clipboard.")

    # Hotkey -> CTRL+6
    @GlobalHotKeys.register(GlobalHotKeys.VK_6, GlobalHotKeys.MOD_CTRL)
    def CopyDistributor():
        clipboard.copy("DigiKey")
        keyboard.write("DigiKey")
        print("'DigiKey' copied to clipboard.")

    # Hotkey -> CTRL+7
    @GlobalHotKeys.register(GlobalHotKeys.VK_7, GlobalHotKeys.MOD_CTRL)
    def CopyDistributorPN():
        clipboard.copy("Distributor Part Number")
        keyboard.write("Distributor Part Number")
        print("'Distributor Part Number' copied to clipboard.")

    # Hotkey -> CTRL+8
    @GlobalHotKeys.register(GlobalHotKeys.VK_8, GlobalHotKeys.MOD_CTRL)
    def CopyDistributorPN():
        clipboard.copy(dk.DigiKeyPN)
        keyboard.write(dk.DigiKeyPN)
        print("'%s' copied to clipboard." % dk.DigiKeyPN)

    # Hotkey -> CTRL+9
    @GlobalHotKeys.register(GlobalHotKeys.VK_9, GlobalHotKeys.MOD_CTRL)
    def CopyDescription():
        clipboard.copy(dk.Description)
        keyboard.write(dk.Description)
        print("Description info copied to clipboard.")

    # Hotkey -> CTRL+0
    @GlobalHotKeys.register(GlobalHotKeys.VK_0, GlobalHotKeys.MOD_CTRL)
    def ReStart():
        dk.AskForURL()

    # ctrl+q will exit script
    GlobalHotKeys.register(GlobalHotKeys.VK_Q, GlobalHotKeys.MOD_CTRL, False)

    #Ask user to provide URL for the first time
    if (len(sys.argv) >= 2):
        dk.SetUrl(sys.argv[1])
    else:
        dk.AskForURL()

    #Main Loop
    GlobalHotKeys.listen()


if __name__ == "__main__" :
    signal.signal(signal.SIGINT, ctrl_c_handler)
    main()

