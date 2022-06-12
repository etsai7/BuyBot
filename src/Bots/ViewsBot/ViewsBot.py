from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup

# Note: If running from Pycharm, will need to Edit Run Configurations and change the Working Directory
#       to start from /src instead of this current folder

edgeDriver = Service('Drivers\\edgedriver_win64\\msedgedriver.exe')
edge = webdriver.Edge(service=edgeDriver)

edge.get('https://www.youtube.com/c/mkbhd/videos')

soup = BeautifulSoup(edge.page_source, features="html.parser")

# Grab the container containing all listed items
videos = soup.find_all("ytd-grid-video-renderer", {"class": "style-scope ytd-grid-renderer"})

videosProcessed = []
for video in videos:
    print(video.find("a", {"id": "video-title"}).text)