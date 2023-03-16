from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "YOUR PATH"
URL = "https://www.instagram.com"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD!"
SEARCH = "YOUR SEARCH TERM"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)

    def login(self):
        self.driver.get(URL)
        # Send login details
        try:
            time.sleep(4)
            self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
            time.sleep(1)
            self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        except Exception as e:
            print(f"Can't Login {e}")
        time.sleep(10)
    
    def find_followers(self):
        # CLICK SEARCH
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Search"]').click()
        except Exception as e:
            print(f"Can't Click on Search {e}")
        # TYPE IN SEARCH FIELD
        try:
            self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]').send_keys(SEARCH)
        except Exception as e:
            print(f"Can't type in search {e}")
        time.sleep(5)
        # LOCATE THE ACCOUNT
        try:
            self.driver.find_element(By.XPATH, "//span[contains(@class, 'x193iq5w') and contains(text(), 'python.hub')]").click() # YOU SHOULD BE ABLE TO REPLACE PYTHON.HUB WITH THE ACCOUNT NAME YOU WANT TO CLICK ON
        except Exception as e:
            print(f"Can't locate account {e}")
        time.sleep(10)
        # CLICK ON ALL FOLLOWERS
        try:
            self.driver.find_element(By.LINK_TEXT, "1.4M followers").click() # YOU CAN REPLACE THE FOLLOWER AMOUNT WITH THE ACTUAL AMOUNT OF FOLLOWERS THE ACCOUNT HAS
        except Exception as e:
            print(f"Cant find followers {e}")
        time.sleep(5)

    def follow_people(self):
        # LOOP THROUGH FOLLOWERS
        try:
            all_followers = self.driver.find_elements(By.CLASS_NAME, 'xl56j7k')
            for followers in all_followers:
                if followers.text == "Follow":
                    followers.click()
                    time.sleep(1)
                    self.driver.execute_script("window.scrollBy(0,10)")
        except Exception as e:
            print(f"Cant locate followers {e}")
        # OPTIONAL EXTENTION - ADD STEP TO CLOSE POPUP WINDOW IF ALL HAS BEEN FOLLOWED AND PUT THE WHOLE METHOD
        # INSIDE A LOOP. DO SIMPLE CALCULATION TO FIND OUT HOW MANY PEOPLE IT FOLLOWS PER LOOP AND HOW MANY
        # TIMES THE LOOP SHOULD BE EXECUTED. IE. 10 FOLLOWERS PER GO / TOTAL FOLLOWERS

        



bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow_people()