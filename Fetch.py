import os
import sys
import signal
import clipboard
import keyboard
import argparse
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
#   Version : 0.4
#
#	Usage	: Run Fetch.py script. When prompted, enter valid DigiKey part URL
#			  Script will retrieve part information and then you can use shortcuts to copy
#			  part information to clipboard
#

# Configure if you want to copy text to clipboard and/or type it with your keyboard
CFG_CopyToClipboard  = True
CFG_TypeWithKeyboard = True

# Function that will copy and or type string for you
def copyAction(str):
    if CFG_TypeWithKeyboard == True:
        keyboard.write(str)
        print("Typing %s" % str)

    if CFG_CopyToClipboard == True:
        print("%s copied to clipboard" % str)
        clipboard.copy(str)


# catch ctrl-c
def ctrl_c_handler(signal, frame):
    print("Goodbye!")
    exit()


def main(cfg):
    global CFG_CopyToClipboard, CFG_TypeWithKeyboard

    if(cfg.nokey):
        print("Script will NOT emulate keyboard keystrokes")
        CFG_TypeWithKeyboard = False

    if(cfg.nocopy):
        print("Script will NOT copy to clipboard")
        CFG_CopyToClipboard = False


    #Initialize DigiKey fetch class
    dk = digikey()

    # Hotkey -> CTRL+1
    @GlobalHotKeys.register(GlobalHotKeys.VK_1, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturer():
        copyAction("Manufacturer")

    # Hotkey -> CTRL+2
    @GlobalHotKeys.register(GlobalHotKeys.VK_2, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturer():
        copyAction(dk.Manufacturer)

    # Hotkey -> CTRL+3
    @GlobalHotKeys.register(GlobalHotKeys.VK_3, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturerPN():
        copyAction("Manufacturer Part Number")

    # Hotkey -> CTRL+4
    @GlobalHotKeys.register(GlobalHotKeys.VK_4, GlobalHotKeys.MOD_CTRL)
    def CopyManufacturerPN():
        copyAction(dk.ManufacturerPN)

    # Hotkey -> CTRL+5
    @GlobalHotKeys.register(GlobalHotKeys.VK_5, GlobalHotKeys.MOD_CTRL)
    def CopyDistributor():
        copyAction("Distributor")

    # Hotkey -> CTRL+6
    @GlobalHotKeys.register(GlobalHotKeys.VK_6, GlobalHotKeys.MOD_CTRL)
    def CopyDistributor():
        copyAction("DigiKey")

    # Hotkey -> CTRL+7
    @GlobalHotKeys.register(GlobalHotKeys.VK_7, GlobalHotKeys.MOD_CTRL)
    def CopyDistributorPN():
        copyAction("Distributor Part Number")

    # Hotkey -> CTRL+8
    @GlobalHotKeys.register(GlobalHotKeys.VK_8, GlobalHotKeys.MOD_CTRL)
    def CopyDistributorPN():
        copyAction(dk.DigiKeyPN)

    # Hotkey -> CTRL+9
    @GlobalHotKeys.register(GlobalHotKeys.VK_9, GlobalHotKeys.MOD_CTRL)
    def CopyDescription():
        copyAction(dk.Description)

    # Hotkey -> CTRL+0
    @GlobalHotKeys.register(GlobalHotKeys.VK_0, GlobalHotKeys.MOD_CTRL)
    def ReStart():
        dk.AskForURL()

    # ctrl+q will exit script
    GlobalHotKeys.register(GlobalHotKeys.VK_Q, GlobalHotKeys.MOD_CTRL, False)

    # Use provided or argparsesk user to provide URL
    if(cfg.url):
        dk.SetUrl(cfg.url)
    else:
        dk.AskForURL()

    # Main Loop
    GlobalHotKeys.listen()

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__" :
    argParser = argparse.ArgumentParser(description="DigiKey Fetch Tool")
    argParser.add_argument("-k", "--nokey", help="Disable keyboard input (script will not type in data for you)", required=False, default=False, action='store_true')
    argParser.add_argument("-c", "--nocopy", help="Disable copying data to clipboard", required=False, default=False,  action='store_true')
    argParser.add_argument("-u", "--url", help="Provide start DigiKey URL (otherwise script will promt to provide one)", required=False, default=False, type=str)

    args = argParser.parse_args()

    signal.signal(signal.SIGINT, ctrl_c_handler)
    main(args)

