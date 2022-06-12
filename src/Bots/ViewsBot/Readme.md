# Views Bot

## Description
This Bot is used to extract the view count by video title, given the link to the youtuber's videos. Mkbhd [example](https://www.youtube.com/c/mkbhd/videos)

[//]: # (![img.png]&#40;imgs/mkbhdVideos.png&#41; - Commented out Example)

 <img src="imgs/mkbhdVideos.png" width="700" > 

And to plot the view count by video using Plotly

 <img src="imgs/mkbhdLineGraph.png" width="700" > 

## Setup

### Modules

[`selenium`](https://www.selenium.dev/) - Allows for python to interface with FireFox

[`beautifulSoup4`](https://www.crummy.com/software/BeautifulSoup/) - Used for structuring the data scraped from the web
page

`pandas` - Data Science and Data Analysis module

[`plotly`](https://plotly.com/python/) - Graphing module for Python

Either will need to npm install these modules or if using Pycharms `File -> Settings -> Project -> Project Interpreter`
to add the module

### WebDriver

This program uses the MS Edge Driver which can be on the [Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) Page


1. For Windows, download the Edge driver that matches your Edge version zip file
2. Extract the folder into a location of your choosing
3. Add folder to Path and restart your system or modifiy this line:
    - ``edgeDriver = Service('Drivers\\edgedriver_win64\\msedgedriver.exe')``
    - **Currently**, this repo contains the driver, though it will be outdated as Edge is updated

## Sources
[Module and Driver Installation Guide](https://www.geeksforgeeks.org/how-to-install-selenium-in-python/)