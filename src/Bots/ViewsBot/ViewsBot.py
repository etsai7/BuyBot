from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup

# Note: If running from Pycharm, will need to Edit Run Configurations and change the Working Directory
#       to start from /src instead of this current folder

# 1. Setup Edge Web Driver and grab the Website
edgeDriver = Service('Drivers\\edgedriver_win64\\msedgedriver.exe')
edge = webdriver.Edge(service=edgeDriver)
edge.get('https://www.youtube.com/c/mkbhd/videos')

# 2. Create BeautifulSoup for Html Parser
soup = BeautifulSoup(edge.page_source, features="html.parser")

# 3. Grab the list of Youtube Videos
videos = soup.find_all("ytd-grid-video-renderer", {"class": "style-scope ytd-grid-renderer"})

# 4. Extract fields from the videos:
#       - Title
#       - View Count
videosProcessed = []
for video in videos:
    videoMetaData = []
    videoTitle = video.find("a", {"id": "video-title"}).text
    videoViewCount = video.find("span", {"class": "style-scope ytd-grid-video-renderer"}).text

    videoMetaData.append(videoTitle)
    videoMetaData.append(videoViewCount)

    print(videoMetaData)
    # print(video.find("a", {"id": "video-title"}).text)