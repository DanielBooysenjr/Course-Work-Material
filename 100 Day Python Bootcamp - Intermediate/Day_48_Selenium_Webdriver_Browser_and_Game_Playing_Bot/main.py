# Selenium Webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By



driver_path = "chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get("http://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
