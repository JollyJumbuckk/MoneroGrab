import xbmcaddon
import xbmcgui

from bs4 import BeautifulSoup

 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

import requests
site = "http://coingecko.com/en/price_charts/monero/usd"


requests = requests.get(site)

soup = BeautifulSoup(requests.text, 'html.parser')

name =soup.find_all('b')[1]

name_strip = name.text.strip()

print (name_strip)

line1 = " The current price: "
line2 = (name_strip)

 
xbmcgui.Dialog().ok(addonname, line1, line2)