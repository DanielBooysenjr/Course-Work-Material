from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)

time.sleep(5)

while True:
    driver.find_element(By.ID, "bigCookie").click()

