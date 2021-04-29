import os
import sys
import ctypes
from ctypes import wintypes
import win32con
from lxml import html
import requests
import json
import clipboard
from fake_useragent import UserAgent

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
#   Version : 0.3
#


class digikey:

    # Initialize class to defaults
    def __init__(self, digiurl=""):
        self.url    = digiurl

        #Parameters
        self.Manufacturer   = ''
        self.ManufacturerPN = ''
        self.DigiKeyPN      = ''
        self.Description    = ''

    # Set which URL to scrape
    def SetURL(self, url):
        self.url = url

    # Start gathering data
    def StartScrape(self):
        ua = UserAgent()

        custom_header   = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
                          }

        print("Scraping {}".format(self.url))

        self.page   = requests.get(self.url, headers = custom_header)
        self.tree   = html.fromstring(self.page.content)

        text_file = open("response.html", "w")
        text_file.write(str(self.page.text.encode('utf8')))
        text_file.close()
        # print("done")
        # exit()

        # Using X-Path (old)
        # #Define some x-path related stuff
        # XP_PD_T = "//table[@id='product-overview']//"

        # Manufacturer   = self.tree.xpath(XP_PD_T + "h2[@itemprop='manufacturer']//span[@itemprop='name']/text()")
        # ManufacturerPN = self.tree.xpath(XP_PD_T + "th[contains(text(),'Manufacturer Part Number')]/following-sibling::td[1]/text()")
        # DigiKeyPN      = self.tree.xpath(XP_PD_T + "th[contains(text(),'Digi-Key Part Number')]/following-sibling::td/meta/@content")
        # Description    = self.tree.xpath(XP_PD_T + "th[contains(text(),'Description')]/following-sibling::td/text()")

        # Using script data
        Application_ld_json = self.tree.xpath("//html//head//script[@type='application/ld+json']/text()")
        jsonData = json.loads(Application_ld_json[0])
        ProductData = jsonData["@graph"][2]

        Manufacturer   = ProductData["brand"]["name"]
        ManufacturerPN = ProductData["mpn"]
        DigiKeyPN      = ProductData["sku"]
        Description    = ProductData["description"]

        self.Manufacturer     = ''.join(Manufacturer).strip()
        self.ManufacturerPN   = ''.join(ManufacturerPN).strip()
        self.DigiKeyPN        = ''.join(DigiKeyPN).strip().replace("sku:", "")
        self.Description      = ''.join(Description).strip()


    # Display what has been scraped. Just for debug and let user verify that information looks fine
    def ShowScrapingInfo(self):
        print("Manufacturer:\t\t" + self.Manufacturer)
        print("Manufacturer PN:\t" + self.ManufacturerPN)
        print("Distributor:\t\tDigiKey")
        print("Distributor PN:\t\t" + self.DigiKeyPN)
        print("Description:\t\t" + self.Description)

        self.ShowShortcuts()


    # Simple validation of DigiKey URL that user has provided
    def ValidateAndSetURL(self, url):
        if url.strip().find("digikey") == -1:
            return -1
        else:
            #print("URL set to "+ url )
            self.SetURL(url)
            return 1


    # Ask user to provide DigiKey URL for fetching data
    def AskForURL(self):
        while True:
            print("Please enter DigiKey URL:")

            digikeyURL = ""
            #wait for use input
            sys.stdout.write('>> ')
            digikeyURL = input().strip()
            print("")

            if self.ValidateAndSetURL(digikeyURL) == 1:
                #Start ftching data
                #print("\r\n-------- Fetching Data --------\r\n")
                self.StartScrape()
                self.ShowScrapingInfo()
                #print("\r\n-------- Fetching Done --------")

                break
            else:
                print("Invalid DigiKey URL!")

    # Set URL
    def SetUrl(self, digikeyURL):
        while True:
            if self.ValidateAndSetURL(digikeyURL) == 1:
                #Start ftching data
                #print("\r\n-------- Fetching Data --------\r\n")
                self.StartScrape()
                self.ShowScrapingInfo()
                #print("\r\n-------- Fetching Done --------")

                break
            else:
                print("Invalid DigiKey URL!")
                exit()


    # Print(out Shortcuts)
    def ShowShortcuts(self):
        print("\r\n---------------------------------------------")
        print("---\t Use following shortcuts \t---")
        print("---   (You can use them in any window) \t---")
        print("---------------------------------------------")
        print("CTRL+1 \t- Copy 'Manufacturer'")
        print("CTRL+2 \t- Copy '%s'" % self.Manufacturer)
        print("CTRL+3 \t- Copy 'Manufacturer Part Number'")
        print("CTRL+4 \t- Copy '%s'" % self.ManufacturerPN)
        print("CTRL+5 \t- Copy 'Distributor'")
        print("CTRL+6 \t- Copy 'DigiKey'")
        print("CTRL+7 \t- Copy 'Distributor Part Number'")
        print("CTRL+8 \t- Copy '%s'" % self.DigiKeyPN)
        print("CTRL+9 \t- Copy Description")
        print("-----------------------------------")
        print("CTRL+0 \t- Fetch new Part (ask for new URL)")
        print("-----------------------------------")
        print("CTRL+Q \t- Quit")


    # Self Explainatory functions
    # Not used at the moment
    # def CopyManufacturer(self):
    #     clipboard.copy(self.Manufacturer)
    #     print("Manufacturer info copied to clipboard.")

    # def CopyManufacturerPN(self):
    #     clipboard.copy(self.ManufacturerPN)
    #     print("ManufacturerPN info copied to clipboard.")

    # def CopyDistributor(self):
    #     clipboard.copy("DigiKey")
    #     print("Distributor info copied to clipboard.")

    # def CopyDistributorPN(self):
    #     clipboard.copy(self.DigiKeyPN)
    #     print("DigiKeyPN info copied to clipboard.")

    # def CopyDescription(self):
    #     clipboard.copy(self.Description)
    #     print("Description info copied to clipboard.")
