from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

import os
# print (os.path.abspath(os.curdir))
# print (os.path.abspath(os.curdir))

# driver = webdriver.Chrome('C:/Users/etsai/Downloads/chromedriver_win32')
# driver = webdriver.Chrome('C:\\Users\\etsai\\Downloads\\chromedriver_win32\\chromedriver.exe')
# driver.get("https://www.newegg.com/p/pl?N=100007709%20601385735%20601357248%20601357247")

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

edgeDriver = Service('C:\\Users\\etsai\\Downloads\\edgedriver_win64\\msedgedriver.exe')
edge = webdriver.Edge(service=edgeDriver)

edge.get('https://youtooz.com/products/cassandra-calin')

# Add to Cart Button
edge.find_element(By.XPATH, '//*[@id="product_form_7306372251848"]/div[2]/div/div[2]/div/button/div/div/span').click()
# Wait for page to refresh
time.sleep(5)
# Select the Go to Shopping Cart
edge.find_element(By.XPATH, '//*[@id="main-content"]/div/section/div/div[3]/div/div/div/a/div/div/span[1]').click()
time.sleep(3)
# Select Check Out Now
edge.find_element(By.XPATH, '//*[@id="cassandra-calin"]/div[4]/div/div[2]/div/form/div[3]/div/div[3]/div/button/div').click()

edge.find_element(By.XPATH, '//*[@id="checkout_reduction_code"]')


'''Typing into a text box'''
edge.get("https://www.google.com")
l = edge.find_element(By.CLASS_NAME, "gLFyf")
# #send input
l.send_keys("Selenium")
# #send keyboard input
# l.send_keys(Keys.RETURN)

# chromeDriver = Service('C:\\Users\\etsai\\Downloads\\chromedriver_win32\\chromedriver.exe')
# chrome = webdriver.Chrome(service=chromeDriver)
#
# chrome.get('https://www.google.com')

# soup = BeautifulSoup(chrome.page_source, features="html.parser")
# items = soup.find("div", {"class": "o3j99 n1xJcf Ne6nSd"})
# print(items)


# Glitch Skull - https://www.youtube.com/channel/UCZ9Uz0x7pCMkpNMgA4G0GSQ/featured


