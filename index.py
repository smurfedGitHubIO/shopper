import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
opts = Options()
opts.add_argument(" --headless")
opts.binary_location= os.getcwd() +'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
chrome_driver = os.getcwd() +"C:\\Users\\HP\\Downloads\\chromedriver_win32"
shops = {'ab':'169850668','mo':'190924746', 'fo':'266213560', 'kj':'204666159'}
# abukay yung may singles
# moldandmore yung may singles pero nasa kada
# fortress vmall yung may mamahaling singles
# kjhobbies yung mura af
what_to_search = input('Search what? Huh? ')
shop = input('In what shop? Huh? (ab, mo, fo, kj) ')
url='https://shopee.ph/search?keyword=' + what_to_search + '&shop=' + shops[shop]
s=Service('C:/Users/HP/Downloads/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(url)
try:
	height = browser.execute_script("return document.documentElement.scrollHeight")
	for i in range(0,height,50):
		q = "window.scrollTo(0," + str(i) + ");"
		browser.execute_script(q) #document.body.scrollHeight
	myElem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'shopee-page-controller')))
	print("Done")
except TimeoutException:
	print("Fuck")
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
