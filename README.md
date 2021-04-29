# DigiKey Fetch Tool

![DigiKey Fetch in action](https://github.com/SasaKaranovic/DigiKeyFetch/blob/master/img/demo.png?raw=true "DigiKey Fetch in action")


Check it out on [SasaKaranovic.com/projects/digikey-fetch-tool/][1]


If task is manual and you repeat it often, it should be automated!
While working on new designs, you often find yourself in a position when you need to create new schematic symbols and/or provide information for their BoM entries. For that you would usually copy-paste information from a supplier website into your eCAD software.
This is one of those tasks that should be automated.
I've created a DigiKey fetch tool. As the name suggest, this script will prompt you for DigiKey URL and then it will fetch information about the part.
But the most useful feature is keyboard shortcuts that work anywhere. You can use shortcuts like CTRL+1, CTRL+2... etc. and the script will Copy&Paste fetched information.

### How does it work?

You run python script, enter DigiKey URL of the part you want to get data from.

Script will open the URL, parse data and fetch information such as Manufacturer, Manufacturer Part Number, DigiKey number and Description.

Shortly you should see fetched information that you can use with assigned shortcuts (CTRL+1, CTRL+2 etc). Now your can either copy&paste this data into clipboard or have the script emulate keystrokes so it will automatically populate fields for you. Hopefully this speeds up your workflow! :)

It's simple, and it works. I like it and it saves me a ton o time and I hope it does the same for you.
That's why I'm sharing it as open-source project and you are free to use or modify the code as you please.

### Running the script and optional flags

You can run the script by running `Fetch.py`. The script should run and ask you to provide first URL.
Once you are done you can use `CTRL+0` shortcut to fetch data from another URL. This way you do not have to restart the script.

This script has an option to copy the data into your clipboard and also emulate keystrokes (type in the data for you).
You can disable keystroke emulation by running the script with `-k`, or disable copying to clipboard by running the script with `-c`
You can also provide the URL to fetch the data from by running the script with `-u URL` flag and URL you want the script to start with.


### Python Requirements

Script is written for Python 3 but should easily be ported to any other Python version.


Using Pip, you can install all dependencies using `pip install -r requirements.txt`


### Suggestions and room for improvement

If task is manual and you repeat it often, it should be automated! This is a quick and dirty script that I needed and ended up creating to fit my workflow. Feel free to use it or modify as you see fit.

This script is not running a "production grade" code. With that said, code could use some optimization as well as some additional features.

I would love to hear how you use it, what do you like and what features would you like to see added next.


## Support the project

[![Buy me a Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=sasakaranovic&button_colour=FFDD00&font_colour=000000&font_family=Inter&outline_colour=000000&coffee_colour=ffffff "Buy me a coffee")][8]

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
  [8]: https://www.buymeacoffee.com/sasakaranovic
