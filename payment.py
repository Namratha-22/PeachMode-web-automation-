from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class details():

    def __init__(self, driver):
        self.driver = driver

    def personal(self, Fullname, Email, Phone, Pincode, Address, Landmark, City, Country, State):

        # Purchase page
        self.driver.find_element_by_xpath("//div/div[@class='inc qtybutton']").click()  # to purchase two dress
        self.driver.find_element_by_css_selector(".secure-checkout").click()  # click on pay
        time.sleep(5)

        # To enter personal details
        self.driver.find_element_by_name('full_name').send_keys(Fullname)
        self.driver.find_element_by_name('email').send_keys(Email)
        self.driver.find_element_by_name('phone').send_keys(Phone)
        self.driver.find_element_by_name('pincode').send_keys(Pincode)
        self.driver.find_element_by_name('street_address').send_keys(Address)
        self.driver.find_element_by_name('landmark').send_keys(Landmark)
        self.driver.find_element_by_name('city').send_keys(City)
        country = Select(self.driver.find_element_by_xpath("//div/select[@class='country country1']"))
        country.select_by_visible_text(Country)
        state = Select(self.driver.find_element_by_xpath("//div/select[@class='state']"))
        state.select_by_value(State)

        default_add = self.driver.find_element_by_xpath("//div/input[1][@value='Home']")  # To verify if Home address is selected
        if default_add.is_selected():
            self.driver.find_element_by_xpath("//div/button[text()='Save and Continue']").click()  # continue to pay
        else:
            default_add.click()
            self.driver.find_element_by_xpath("//div/button[text()='Save and Continue']").click()
        time.sleep(5)

class pay():
    def __init__(self, driver):
        self.driver = driver

    def amount(self,Card_num, Card_name, CVV,exp_year,exp_mth):
        # Proceed to payment
        self.driver.find_element_by_id("card_number").send_keys(Card_num)  # To enter the card number
        self.driver.find_element_by_xpath("//label[text()='Name on Card*']/parent::div/input").send_keys(Card_name)  # To enter the name on card
        month = Select(self.driver.find_element_by_name('card_month'))  # to select the exiry month of the card
        month.select_by_value(exp_mth)
        year = Select(self.driver.find_element_by_name('card_year'))  # to select the exiry year of the card
        year.select_by_value(exp_year)
        self.driver.find_element_by_id('card_cvv').send_keys(CVV)  # to enter the CVV number
        self.driver.find_element_by_id('credit_save_card').click()  # to select default card
        self.driver.find_element_by_id('card_payment_button').click()  # Proceed to payment
        time.sleep(25)
        alt = self.driver.switch_to.alert
        alt.accept()
