import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument(" --headless")
opts.binary_location= os.getcwd() +'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
chrome_driver = os.getcwd() +"C:\\Users\\HP\\Downloads\\chromedriver_win32"

what_to_search = input('Search what? Huh?')
url='https://shopee.ph/search?keyword=' + what_to_search + '&shop=169850668'
s=Service('C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(url)
soup_file = browser.page_source
soup = BeautifulSoup(soup_file, "html.parser")
results = soup.find(id="main")
cards = results.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
for card in cards:
	price = card.find("span", class_="_3c5u7X")
	title = card.find("div", class_="_10Wbs- _2STCsK _3IqNCf")
	if price != None:
	    print(price.text.strip(),title.text.strip())
	else:
		break
browser.quit()