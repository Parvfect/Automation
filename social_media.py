from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


class Connection:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = driver
        self.base_url = 'https://www.instagram.com/'
        self.login()

    def login(self):
        """
        Logs into Instagram
        """

        self.driver.get(self.base_url)

        # Accepts cookies
        self.accept_cookies()
        
        # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
        enter_username = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
    
        enter_username.send_keys(self.username)
        
        # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
        enter_password = WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
    
        # RETURNING THE PASSWORD and login into the account
        enter_password.send_keys(Keys.RETURN)

        time.sleep(5)


    def check_popups():
        """
        Checks for popups and clears them
        """
        
        # checks if popups are present
        if chrome.find_element_by_class_name('HoLwm'):
            # clears the popups
            chrome.find_element_by_class_name('HoLwm').click()
            time.sleep(2)
            print("Popup cleared")
            

    def accept_cookies(self):
        """
        Accepts the cookies given by instagram
        """

        print("Checking for cookies")

        # checks if cookies are already accepted
        if self.driver.get_cookie('sessionid'):
            print("Cookies already accepted")
            return

        else:
            print("Accepting cookies")
            # accepts the cookies
            accept_cookies = WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Accept All']")))
            accept_cookies.click()
            time.sleep(2)
            print("Cookies accepted")
            
    def save_info_screen(self):
        """
        Saves the information of the user
        """
        # saves the information of the user
        save_info = WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        save_info.click()
        time.sleep(2)
        print("Save Info page cleared")

   
    def get_notifications(session):
        """
        Gets instagram notifications given a user session
        """
        
        # gets the notifications
        notifications = WebDriverWait(session.driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Notifications']")))
        notifications.click()
        time.sleep(2)
        
        # gets the number of notifications
        num_notifications = chrome.find_element_by_class_name('FPmhX notranslate  yrJyr').text
        print(num_notifications)


if __name__ == '__main__':
    # ENTER THE USERNAME AND PASSWORD
    username = ''
    password = ''
    bot = Connection(username, password)
    chrome = bot.driver
    bot.save_info_screen()
    bot.save_info_screen()
    bot.get_notifications()
