# Internet speed test and complaint twitter bot
# Used XPATHS because Selenium was making my laptop slow and didn't feel like testing over and over again

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time

url = "YOUR SPEED TEST SITE"
path = "YOUR PATH"
DONWLOAD_EXPECTED = "YOUR EXPECTED DOWNLOAD SPEED AS INT"
UPLOAD_EXPECTED = "YOUR EXPECTED UPLOAD SPEED AS INT"
twitter = "https://twitter.com/home"
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
USERNAME = "YOUR USERNAME"

message = f"Hey Internet Provider, why is my download/upload when I pay for {DONWLOAD_EXPECTED}dl/{UPLOAD_EXPECTED}up?"

class InternetSpeedTest:
    def __init__(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get(url)

    def tweet_at_provider(self):
        self.driver.get(twitter)
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(EMAIL)
        except Exception as e:
            print(f"Cant send login email address {e}")
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        except Exception as e:
            print(f"Cant click next {e}")
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(USERNAME)
        except Exception as e:
            print(f"No element found for username {e}")
            pass
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
        except Exception as e:
            print(f"No next {e}")
            pass
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(PASSWORD)
        except Exception as e:
            print(f"Cant get password field {e}")
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span').click()
        except Exception as e:
            print(f"Can't click login {e}")
        time.sleep(15)
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]/div').click()
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]/div').send_keys(self.new_message)
        except Exception as e:
            print(f"Cant start tweet {e}")
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
        except Exception as e:
            print(f"Can not post tweet {e}")
        time.sleep(3000)


        
    def get_internet_speed(self):
        time.sleep(3)
        # Press Start
        try:
            self.driver.find_element(By.XPATH, '//*[@id="start-btn"]').click()
        except Exception as e:
            print(f"Cant press start{e}")
        time.sleep(30)
        try:
            self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="download-result"]')
            self.download_speed_int = float(self.download_speed.text)
            print(self.download_speed_int)
            # return self.download_speed_int
        except Exception as e:
            print(f"Cant get download speed{e}")

        try:
            self.upload_Speed = self.driver.find_element(By.XPATH, '//*[@id="upload-result"]')
            self.upload_speed_int = float(self.upload_Speed.text)
            print(type(self.upload_speed_int))
            print(self.upload_speed_int)
            # return self.upload_speed_int
        except Exception as e:
            print(f"Cant get download speed{e}")

        time.sleep(5)

        if self.download_speed_int < DONWLOAD_EXPECTED or self.upload_speed_int < UPLOAD_EXPECTED:
            self.replace_dl = message.replace("download", self.download_speed.text)
            self.new_message = self.replace_dl.replace("upload", self.upload_Speed.text)
            print(self.new_message)
            ini.tweet_at_provider()
        else:
            print("Internet speed is fine.")
            return


ini = InternetSpeedTest()
ini.get_internet_speed()

