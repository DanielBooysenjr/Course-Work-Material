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



def copy_text():
    os.startfile(gvars.post)
    time.sleep(2)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    pg.hotkey('alt','f4')
    time.sleep(2)

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
            # NAVIGATE TO FIRST GROUP
            self.driver.get(groups)
            time.sleep(5)
        except Exception as e:
            print("Couldn't navigate to the group")

    def Initialize(self):

        # Click on write something text box to initiate post
        try:
            self.driver.find_element(By.XPATH, gvars.xpath).click()
            print("Clicked on post now button successfully")
            time.sleep(5)
        except Exception as e:
            print("Could not initialize group posting: " + str(e))

    def Post(self):       
        # Click on Photo Icon

        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, gvars.icon).click()
            time.sleep(2)
        except Exception as e:
            print("Couldn't click on photo icon")
        
        # CLICK ON ADD PHOTO BUTTON
        try:
            photo = self.driver.find_element(By.XPATH, gvars.photo).click()
            time.sleep(2)
        except Exception as e:
            print("Couldn't Click on add photo button")


        # NAVIGATE TO VILUX PHOTOS DIRECTORY
        try:
            pg.click(x=2536, y=102, clicks=1, button='left', duration = 0.5)
            time.sleep(1)
            pg.write(gvars.path)
            pg.press('enter')
            time.sleep(2)
        except Exception as e:
            print("Couldn't Navigate to folder")

            # NAVIGATE TO FIRST IMAGE IN FOLDER
        try:
            pg.click(x=611, y=428, clicks=1, button='left', duration = 0.5)
            time.sleep(2)
        except Exception as e:
            print("Couldn't Click on image")

        try:
            # SELECT IMAGE
            pg.press(gvars.image)
            pg.press('enter')
        except Exception as e:
            print("Problem selecting gvars image")

            # PASTE IN ADVERTISEMENT TEXT
        try:
            text = self.driver.find_element(By.XPATH, gvars.paste).click()
            time.sleep(4)
            pg.hotkey('ctrl','shift','v')
        except Exception as e:
            print("Couldn't Paste text")

        try:
            # Post to group
            self.driver.find_element(By.XPATH, gvars.post).click()
            time.sleep(10)
        except Exception as e:
            print("Could not initialize: " + str(e))
'''        try:
            post = self.driver.find_element(By.XPATH, gvars.post)
            if post.is_displayed():
                pass
            else:
        except Exception as e:
            print("Moving on")'''


class main_gui:
    def __init__(self):
        
        customtkinter.set_appearance_mode(gvars.dark)  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # Create the main window
        self.app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.app.geometry("800x600")
        self.app.title("Automator 2000")


        # Create a function that will be called when the "Start Program" button is clicked
        def start_program():

            # Initialize the bot
            copy_text()
            global bot
            bot = Facebook_Bot()
            openchrome = bot.Open_Chrome()
            login = bot.Login()

            # Loop through posting on groups (For when the start posting button was clicked in the GUI)
            counter = 1

            for groups in gvars.groups:
                navigate = bot.Group_Navigation(groups)
                initialize = bot.Initialize()
                post = bot.Post()
                print("Group: {} posted on successfully".format(counter))
                counter += 1
                print("Group linK: '{}'".format(groups))
                if counter > 64:
                    print("All groups posted, closing chrome")
                    pg.hotkey('Alt', 'f4')
    
        # Choosing which product must be advertised
        def dropdown(self, value):
            if value == 'Cleaning':
                gvars.path = gvars.cleaning # Sets the path of the images to the path of the products images specified
                gvars.post = gvars.postcleaning # Changes the file that needs to be used to copy the advertisement text
            if value == 'Lighters':
                gvars.path = gvars.lighters
                gvars.post = gvars.postcleaning
            if value == 'Blankets':
                gvars.path = gvars.blankets
                gvars.post = gvars.postcleaning
            if value == 'Bracelets':
                gvars.path = gvars.bracelets
                gvars.post = gvars.postcleaning
            if value == 'Babygrows':
                gvars.path = gvars.babygrows
                gvars.post = gvars.postcleaning


        # MAIN WINDOW BUTTONS

        # Create the "Start Program" button and place it in the window
        self.start_button = customtkinter.CTkButton(self.app, width=120, corner_radius=6, height=30, text="Start Advertising", command=start_program)

        self.label = customtkinter.CTkLabel(self.app, text='Choose Which Product You Would Like To Advertise Today', fg_color='white', text_color='black', width=350)
        self.dropdown_button = customtkinter.CTkOptionMenu(self.app,width=120, corner_radius=6, height=30,
                                                    values=['Cleaning', 'Lighters', 'Blankets', 'Bracelets', 'Babygrows'], command=lambda value: dropdown(self, value))

        # Placing the buttons
        self.start_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.label.place(relx=0.05,rely=0.4)
        self.dropdown_button.place(relx=0.5, rely=0.4)





'''        def theme(self,value):
            if value == 'dark':
                gvars.dark = gvars.dark
            if value == 'light':
                gvars.light = gvars.dark
            if value == 'system':
                gvars.system = gvars.dark'''



# Create an instance of the main_gui class
app = main_gui()

# Run the main loop
app.app.mainloop()






'''copy_text = copy_text()
bot = Facebook_Bot()
openchrome = bot.Open_Chrome()
login = bot.Login()'''




