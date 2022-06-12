from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def getItemBrand(item):
    # Grabs the 'a' tag labelled as item-brand
    itemBrandContainer = item.find("a", {"class": "item-brand"})
    # Brand name is stored in the image link
    ''' There are 3 attributes from the img tag
        'src' = {str} 'https://c1.neweggimages.com/Brandimage_70x28/Brand1314.gif'
        'title' = {str} 'GIGABYTE'
        'alt' = {str} 'GIGABYTE'
    '''
    return itemBrandContainer.find("img").attrs['title'] if itemBrandContainer else ''

# 1. Open up website: NewEgg directly to gpu link - prob w/ filters intact
driver = webdriver.Firefox()
driver.get("https://www.newegg.com/p/pl?N=100007709%20601385735%20601357248%20601357247")

# 2. Grab all available gpus using Beautiful Soup
soup = BeautifulSoup(driver.page_source, features="html.parser")

# Grab the container containing all listed items
items = soup.find("div", {"class": "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell"})

# Go through each of the items in the list
itemsProcessed = []
for item in items.findAll("div"):
    itemData = []
    itemTitle = item.find("a", {"class": "item-title"})
    itemAvailability = item.find("p", {"class": "item-promo"})
    itemBrand = getItemBrand(item)

    status = "Available"

    if itemAvailability and itemAvailability == "OUT OF STOCK":
        status = "Sold Out"

    if itemTitle:
        itemData.append(itemBrand)
        itemData.append(itemTitle.text)
        itemData.append(status)

    if itemData:
        itemsProcessed.append(itemData)

pd.set_option('display.max_rows', 100)
df = pd.DataFrame.from_records(itemsProcessed, columns = ["Item Brand", "Item Title", "Status"])
print(df)



# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# 1. Open up website: NewEgg directly to gpu link - prob w/ filters intact
# 2. Grab all available gpus using Beautiful Soup
# 3. Add filters
#     - Only ones in stock
#     - Sort by pricing
#     - Maybe in brand or type

# May need to have a bunch of try catches

# URL: https://www.newegg.com/p/pl?N=100007709%20601385735%20601357248%20601357247
# Container for all listed items: /html/body/div[7]/div[4]/section/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]
# A single item cell: //*[@id="item_cell_14-932-327_1_0"]
