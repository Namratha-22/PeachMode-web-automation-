from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class dress():

    def __init__(self,driver):
        self.driver = driver

    def choice (self):
        #To go to women's Lehenga section
        act=ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath('//a/span[text()="Women"]')).move_to_element(
            self.driver.find_element_by_xpath("//div/span[text()='Lehenga']/parent::div/a[13]")).click().perform()
        time.sleep(10)
        assert 'Lehenga' in self.driver.title #to verify the page

        self.driver.find_element_by_link_text('Party wear Lehenga').click() #Go to party wear section
        handles=self.driver.window_handles
        parent=handles[0]
        child=handles[1]
        self.driver.switch_to.window(child)#switch the self.driver control to child window
        time.sleep(10)
        assert 'Party Wear Lehenga' in self.driver.title #To verify the page

        self.driver.find_element_by_xpath("//div[@class='sidebar-box mt-40 rmt-20']/div/ul/li[4]/label").click() # To select the discount
        self.driver.find_element_by_xpath("//label/input[@value='Semi Stitched']").click() # To select the stitch
        self.driver.find_element_by_xpath("//label/input[@value='Velvet']").click()  #to select the material as Velvet
        self.driver.find_element_by_xpath("//div[@class='sidebar-box mt-40 rmt-20']/label[15]").click() # To select the colour Marroon
        self.driver.find_element_by_css_selector(".tab-menu-review :nth-of-type(2)").click() #To choose filter the price from low to high

        dress=self.driver.find_elements_by_xpath("//div[@class='product-list-all']/div/div/div/div") # to find the matching adress

        for i in dress: # loop through the dress
            i.click()#Go to each dress
            dupatta=self.driver.find_element_by_xpath("//td[text()='Dupatta']") #To find the dupatta colour of dress
            colour=dupatta.find_element_by_xpath('/parent::tr/td/table/tbody/tr/td[@class="td-2"]')
            if colour.text=='Maroon': # to find the matching clour of dupatta
                self.driver.find_element_by_xpath("//a/span[text()='Buy Now']").click()# continue to bye
                break
        else:
            print(" We do not have matching Dupatta")
