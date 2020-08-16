from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

import login_page
import dress_select_page
import payment

opt = webdriver.ChromeOptions()
#opt.add_argument(" headless ")
opt.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:\python practice\py_driver\chromedriver_win32\chromedriver.exe",
                          options=opt)

driver.get("https://peachmode.com")
time.sleep(5)
driver.maximize_window()  # To maximize window

# To login
Username = '.... '
Password = '.... '

checkin = login_page.login(driver)
checkin.log_on(Username, Password)

# To go to women's Lehenga section
dress=dress_select_page.dress(driver)
dress.choice()
# Purchase page

Fullname = ' '
Email = ' '
Phone = ' '
Pincode = ' '
Address = ' '
Landmark = ' '
City = ' '
Country= ' '
States=' '
exp_year=' '
exp_mth=' '
Data = payment.details(driver)
Data.personal(Fullname, Email, Phone, Pincode, Address, Landmark,City,Country,States )

Card_num = ' '
Card_name = ' '
CVV = ' '

bill=payment.pay(driver)
bill.amount(Card_num, Card_name, CVV,exp_year,exp_mth)











