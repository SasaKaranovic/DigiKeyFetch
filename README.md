# DigiKey Fetch Tool

Check it out on [SasaKaranovic.com/projects/digikey-fetch-tool/][1]

Well, as the name suggests, this is a very simple tool that I use to fetch DigiKey
information about parts while making new database components or while generating BOM

### How does it work?

You run python script, enter DigiKey URL of the part you want to get data from.

Script will open the URL, parse data and fetch information such as Manufacturer, Manufacturer Part Number, DigiKey number and Description.

Shortly you should see fetched information and options to copy each individiual piece of information to clipboard
so you just do paste into your favourite eCAD. You don't even have to do copy&paste, just paste. :)

It's simple, and it works. I like it, your mileage might vary.


### Python Requirements

Script is written for Python 2.7 but should easily be ported to any other Python version.

I assume that you have Pip installed ([instructions here][7]) and for this script to work please install following modules:

`pip install lxml`

`pip install clipboard`

`pip install requests`



### Room for improvement

This is a quick&dirty script that I needed and ended up creating in 15 min, therefore don’t expect it to be bullet proof.

Nevertheless it is a very nice and practical tool to have and I use it on daily basis.

I would love to hear how you use it, what do you like and what features would you like to see added next.


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
