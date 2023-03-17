# Data Entry Job Automation using Selenium and BeautifulSoup

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time

FORM_URL = "YOUR FROM URL"
SEARCH_URL = "https://www.zillow.com/YOUR SEARCH CRITERIA"
href = "https://www.zillow.com"
PATH = "YOUR PATH"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

response = requests.get(url=SEARCH_URL, headers=headers)
rental_listings = response.text


soup = BeautifulSoup(rental_listings, "html.parser")

listing_info = soup.find_all(class_="ListItem-c11n-8-85-1__sc-10e22w8-0 srp__sc-wtsrtn-0 jhnswL with_constellation")

address = []
price = []
link = []


for i in listing_info:
    # Getting Address
    try:
        listing_address = i.find("address")
        if listing_address == None:
            continue
    except Exception as e:
        print(e)
    address.append(listing_address.text)

    # Getting Price
    try:
        listing_price = i.find(class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 bqsBln")
    except Exception as e:
        print(e)
    price.append(listing_price.text)

    # Getting URL

    try:
        listing_url = i.find(class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")["href"]
        if href not in listing_url:
            listing_url = f"{href}{listing_url}"
    except Exception as e:
        print(e)
    link.append(listing_url)


driver = webdriver.Chrome(PATH)
driver.get(FORM_URL)

for j in range(len(price)):
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address[j])
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price[j])
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link[j])
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

driver.get('https://docs.google.com/forms/d/1KQXLGBgHVEAe2kAmWPQTT-sy9sT8zHF4481zGmocP9k/edit#responses')

# Rest of the code for interacting with the form
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]').click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[17]/div/div[2]/span/div/div/span/div[1]/div/div/div[1]/div/div[1]/input').clear()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[17]/div/div[2]/span/div/div/span/div[1]/div/div/div[1]/div/div[1]/input').send_keys("New Form")
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[17]/div/div[2]/div[3]/div[2]/span/span').click()

    






