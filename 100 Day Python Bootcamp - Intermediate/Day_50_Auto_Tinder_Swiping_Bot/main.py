# Tinder Automated Swiping Bot

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://tinder.com/"
path = "C:\\chromedriver.exe"
phone = "YOUR NUMBER"

driver = webdriver.Chrome("YOUR CHROMEDRIVER PATH")
driver.get(url)

time.sleep(2)
# Login
for i in range(101):
    try:
        driver.find_element(By.LINK_TEXT, "Log in").click()
    except Exception as e:
        print(f"Problem login in. {e}")
        pass
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button').click()
    except Exception as e:
        print(f"Problem clicking on login with phone number. {e}")
        pass
    time.sleep(90)
    # Enter Phone Number
    try:
        driver.find_element(By.NAME, "phone_number").send_keys(phone)
    except Exception as e:
        print(f"Cant enter phone number {e}")
        pass
    time.sleep(2)
    # Hit Login
    try:
        driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div[1]/div/button').click()
    except Exception as e:
        print(f"Cant click continue {e}")
        pass
    time.sleep(45)
    # Allow Location
    try:
        driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div/div[3]/button[1]').click()
    except Exception as e:
        print(f"Couldn't click allow {e}")
        pass
    time.sleep(1)
    # Not interested in notifications
    try:
        driver.find_element(By.XPATH, '//*[@id="s-1211347640"]/main/div/div/div/div[3]/button[2]').click()
    except Exception as e:
        print(f"Cant click not interested {e}")
        pass
    time.sleep(3)
    # Click Swipe Right
    try:
        driver.find_element(By.XPATH, '//*[@id="s-1432688076"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path').click()
    except Exception as e:
        print(f"Cant swipe right {e}")
        pass
    time.sleep(3)
    # Check if match, and return to tinder if match found
    try:
        driver.find_element(By.LINK_TEXT, "BACK TO TINDER").click()
    except Exception as e:
        print("Not a match")
        pass
    time.sleep(3)

