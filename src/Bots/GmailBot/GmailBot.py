from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# driver = webdriver.Edge(executable_path="D:\\Eric Tsai\\Programming\\Personal\\Projects\BuyBot\\edgedriver_win64\\msedgedriver.exe")

PASSWORD = "P@ssword70";
USERNAME = "jlee19742022"

ser = Service(executable_path="/edgedriver_win64/msedgedriver.exe")
ff_Service=Service(executable_path="/geckodriver-v0.31.0-win64/geckodriver.exe")
# driver = webdriver.Edge(service=service)
driver = webdriver.Firefox(service=ff_Service)
# driver.get("https://www.google.com/")
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%26ogbl%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element(By.XPATH, "//*[@id=\"identifierId\"]").send_keys("myEmail@gmil.com")
driver.find_element(By.XPATH, "//*[@id=\"identifierNext\"]/div/button/span").click()