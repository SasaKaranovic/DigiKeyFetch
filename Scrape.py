from Classes.digikey import digikey

#Initialize state machine
varState = 0

#Initialize DigiKey scraping class
dk = digikey()

print "Please enter DigiKey URL:"

#wait for use input
digikeyURL = raw_input().strip()

#validate URL
dk.ValidateAndSetURL(digikeyURL)



#Show options
while(1):
    #Start Scraping
    print "\r\n-------- Fetching Data --------\r\n"
    dk.SetURL(digikeyURL)
    dk.StartScrape()
    dk.ShowScrapingInfo()
    print "\r\n-------- Fetching Done --------"


    dk.PrintCopyOptions()
    option = input()
    dk.ParseCopyOptions(option)

    #Another URL request
    if option == 8:
        print "Please enter DigiKey URL:"

        #wait for use input
        digikeyURL = raw_input().strip()

        dk.ValidateAndSetURL(digikeyURL)
   

