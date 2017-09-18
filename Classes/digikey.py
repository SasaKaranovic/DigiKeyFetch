import os
import sys
import ctypes
from ctypes import wintypes
import win32con
from lxml import html
import requests
import clipboard

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


class digikey:

    #Initialize class to defaults
    def __init__(self, digiurl=""):
        self.url    = digiurl

        #Parameters
        self.Manufacturer   = ''
        self.ManufacturerPN = ''
        self.DigiKeyPN      = ''
        self.Description    = ''

    #Set which URL to scrape
    def SetURL(self, url):
        self.url = url

    #Start gathering data
    def StartScrape(self):
        self.page   = requests.get(self.url)
        self.tree   = html.fromstring(self.page.content)

        #Define some x-path related stuff
        XP_PD_T = "//table[@id='product-details']//"

        Manufacturer   = self.tree.xpath(XP_PD_T + "h2[@itemprop='manufacturer']//span[@itemprop='name']/text()")
        ManufacturerPN = self.tree.xpath(XP_PD_T + "th[contains(text(),'Manufacturer Part Number')]/following-sibling::td/meta/@content")
        DigiKeyPN      = self.tree.xpath(XP_PD_T + "th[contains(text(),'Digi-Key Part Number')]/following-sibling::td/meta/@content")
        Description    = self.tree.xpath(XP_PD_T + "th[contains(text(),'Description')]/following-sibling::td/text()")

        self.Manufacturer     = ''.join(Manufacturer).strip()
        self.ManufacturerPN   = ''.join(ManufacturerPN).strip()
        self.DigiKeyPN        = ''.join(DigiKeyPN).strip().replace("sku:", "")
        self.Description      = ''.join(Description).strip()


    #Display what has been scraped. Just for debug and let user verify that information looks fine
    def ShowScrapingInfo(self):
        print "Manufacturer: \t\t" + self.Manufacturer
        print "Manufacturer PN: \t" + self.ManufacturerPN
        print "DigiKey PN: \t\t" + self.DigiKeyPN
        print "Description: \t\t" + self.Description

        self.ShowShortcuts()


    #Simple validation of DigiKey URL that user has provided
    def ValidateAndSetURL(self, url):
        if url.strip().find("digikey") == -1:
            return -1
        else:
            #print "URL set to "+ url 
            self.SetURL(url)
            return 1


    #Ask user to provide DigiKey URL for fetching data
    def AskForURL(self):
        while True:
            print "Please enter DigiKey URL:"

            digikeyURL = ""
            #wait for use input
            sys.stdout.write('>> ')
            digikeyURL = raw_input().strip()
            print ""

            if self.ValidateAndSetURL(digikeyURL) == 1:
                #Start ftching data
                #print "\r\n-------- Fetching Data --------\r\n"
                self.StartScrape()
                self.ShowScrapingInfo()
                #print "\r\n-------- Fetching Done --------"

                break
            else:
                print "Invalid DigiKey URL!"


    #Print out Shortcuts
    def ShowShortcuts(self):
        print "\r\n---------------------------------------------"
        print "\r\n---\t Use following shortcuts \t---"
        print "---   (You can use them in any window) \t---"
        print ""
        print "ALT+1 \t- Copy Manufacturer"
        print "ALT+2 \t- Copy Manufacturer Part Number"
        print "ALT+3 \t- Copy Distributor"
        print "ALT+4 \t- Copy Distributor Part Number"
        print "ALT+5 \t- Copy Description"
        print "-----------------------------------"
        print "ALT+0 \t- Fetch new Part"
        print "-----------------------------------"
        print "CTRL+Q \t- Quit"


    #Self Explainatory functions
    #Not used at the moment
    # def CopyManufacturer(self):
    #     clipboard.copy(self.Manufacturer)
    #     print "Manufacturer info copied to clipboard."

    # def CopyManufacturerPN(self):
    #     clipboard.copy(self.ManufacturerPN)
    #     print "ManufacturerPN info copied to clipboard."

    # def CopyDistributor(self):
    #     clipboard.copy("DigiKey")
    #     print "Distributor info copied to clipboard."

    # def CopyDistributorPN(self):
    #     clipboard.copy(self.DigiKeyPN)
    #     print "DigiKeyPN info copied to clipboard."

    # def CopyDescription(self):
    #     clipboard.copy(self.Description)
    #     print "Description info copied to clipboard."



