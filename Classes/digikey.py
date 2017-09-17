import sys
import os
from lxml import html
import requests
import clipboard

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


    def ValidateAndSetURL(self,url):
        if url.find("digikey") == -1:
            print "Invalid URL!"
            return 0

        print "URL set to "+ url 
        self.url = url
        return 1


    #Print available options to the user
    def PrintCopyOptions(self):
        print "\r\nWhat would you like to copy to clipboard?\r\n"

        print "[1] - Manufacturer"
        print "[2] - Manufacturer Part Number"
        print "[3] - Distributor [always DigiKey]"
        print "[4] - Distributor Part Number"
        print "[5] - Description"
        print "-------------------------------------"
        print "[8] - Fetch another DigiKey Part"
        print "-------------------------------------"
        print "[0] - Quit"

    #Based on user input, copy scraped information to clipboard
    def ParseCopyOptions(self, option):
        if option == 1:
            clipboard.copy(self.Manufacturer)
            print "Manufacturer info copied to clipboard.\r\n"

        elif option == 2:
            clipboard.copy(self.ManufacturerPN)
            print "Manufacturer Part Number info copied to clipboard.\r\n"

        elif option == 3:
            clipboard.copy("DigiKey")
            print "Distributor info copied to clipboard.\r\n"

        elif option == 4:
            clipboard.copy(self.DigiKeyPN)
            print "Distributor Part Number info copied to clipboard.\r\n"

        elif option == 5:
            clipboard.copy(self.Description)
            print "Description info copied to clipboard.\r\n"

        elif option == 0:
            exit()
        else:
            print "Invalid option selected."
