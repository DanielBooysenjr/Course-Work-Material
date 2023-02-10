###

#BELOW CODE LOGS INTO FACEBOOK USING SELENIUM LIB

###

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg
import time
import os
import gvars
import tkinter as tk
import customtkinter


class Facebook_Bot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")

    def Open_Chrome(self):
        
        self.driver.get(gvars.url)

        # Maximize the browser window
        self.driver.maximize_window()

        time.sleep(5)

    def Login(self):

        driver = webdriver.Chrome

        # Find login buttons of Username, Password and Clicks Login
        try:
            self.driver.find_element(By.NAME, 'email').send_keys(gvars.username)
            self.driver.find_element(By.NAME, 'pass').send_keys(gvars.password)
            self.driver.find_element(By.NAME, 'login').click()
        except Exception as e:
            print("Couldn't Log in to account")

        print('Logged in successfully')
        time.sleep(10)

        # Close the popup window
        pg.press('TAB')
        pg.press('ENTER')
        print('Popup window closed successfully')

    def Group_Navigation(self,groups):

        try:
            time.sleep(5)
            # NAVIGATE TO FIRST GROUP
            self.driver.get(groups)
            time.sleep(5)
        except Exception as e:
            print("Couldn't navigate to the group")

def Initialize(self):
    for i in range(10):
        try:
            button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Photo/video')]")
            if button:
                if button.is_enabled():
                    button.click()
                else:
                    print("Button is not clickable")
            else:
                print("Button with text 'Photo/video' not found")
            break
        except:
            time.sleep(2)
            continue
    else:
        print("Button not found after 10 attempts")



'''        try:
            self.driver.find_element(By.XPATH, gvars.xpath).click()
            print("Clicked on post now button successfully")
            time.sleep(5000)
        except Exception as e:
            try:
                self.driver.find_element(By.XPATH, gvars.xpath1).click()
            except Exception as e:
                print("Could not initialize group posting: " + str(e))'''






        



def start_program():

    # Initialize the bot
    global bot
    bot = Facebook_Bot()
    bot.Open_Chrome()
    bot.Login()
    bot.Group_Navigation(groups=gvars.groups[0])
    bot.Initialize()




start_program()