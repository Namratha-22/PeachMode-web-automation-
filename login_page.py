from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class login():
    def __init__(self, driver):
        self.driver = driver

    def log_on(self, Username, Password):
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath("//ul[@class='my-setting']/li/span/i")).move_to_element(
            self.driver.find_element_by_xpath("//li/a[text()='Log In']")).click().perform()  # to click on login button
        self.driver.find_element_by_name('username').send_keys(Username)  # To input username
        self.driver.find_element_by_id('id_password').send_keys(Password)  # To input password
        self.driver.find_element_by_xpath("//form/input[@value='Log in']").submit()  # submit to login
        time.sleep(10)