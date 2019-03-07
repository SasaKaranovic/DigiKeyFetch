# DigiKey Fetch Tool

Check it out on [SasaKaranovic.com/projects/digikey-fetch-tool/][1]

If task is manual and you repeat it often, it should be automated!
While working on new designs, you often find yourself in a position when you need to create new schematic symbols and/or provide information for their BoM entries. For that you would usually copy-paste information from a supplier website into your eCAD software.
This is one of those tasks that should be automated.

I've created a DigiKey fetch tool. As the name suggest, this script will prompt you for DigiKey URL and then it will fetch information about the part.
Conveniently it also provides shortcuts (that will work in any window), so you don't have to ALT+TAB from your favorite eCAD at all. Just press CTRL+2 and Manufacturer name will be copied, CTL+4 and Part Number will be copied into your clipboard and so on.

### How does it work?

You run python script, enter DigiKey URL of the part you want to get data from.

Script will open the URL, parse data and fetch information such as Manufacturer, Manufacturer Part Number, DigiKey number and Description.

Shortly you should see fetched information and options to copy each individiual piece of information to clipboard
so you just do paste into your favourite eCAD. You don't even have to do copy&paste, just paste. :)

It's simple, and it works. I like it, your mileage might vary.


### Python Requirements

Script is written for Python 3 but should easily be ported to any other Python version.


Using Pip, you can install all dependencies using `pip install -r requirements.txt`,
or if you prefer, manually one by one (dependencies are: requests, clipboard, pypiwin32, lxml, requests)


### Room for improvement

If task is manual and you repeat it often, it should be automated! While co
This is a quick and dirty script that I needed and ended up creating in 15 min, therefore don’t expect it to be bullet proof.

Nevertheless it is a very nice and practical tool to have and I use it on daily basis.

I would love to hear how you use it, what do you like and what features would you like to see added next.

Currently script is not fetching information from DigiKey urls that have `?keywords=` in them due the way
DigiKey is handling search queries (Try disabling JavaScript in your browser and visit the same URL, it will present a "blank" page).

In order to avoid any OS related issues, string is copied into clipboard. It would be nice to have the script
emulate keystrokes so it types the string for you.

## Find out more cool projects 

Find more cool projects on my [website][1].

Also feel free to follow me on social media:
[SasaKaranovic.com][2] - [YouTube][3] - [Facebook][4] - [Twitter][5] - [LinkedIn][6]

  [1]: http://sasakaranovic.com/projects/digikey-fetch-tool/
  [2]: http://sasakaranovic.com/
  [3]: http://sasakaranovic.com/youtube
  [4]: http://sasakaranovic.com/facebook
  [5]: http://sasakaranovic.com/twitter
  [6]: http://sasakaranovic.com/linkedin
  [7]: https://pip.pypa.io/en/stable/installing/
