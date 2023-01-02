
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#Implicit wait  -
#Explicit Wait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\XT23495\\Downloads\\chromeDriver\\chromedriver.exe")
driver.get("http://hwd-itcm111q/reports/phoenix_AG_status/get_phoenix_AG_status/itcm_remote_info.html")
time.sleep(5)
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//a[contains(text(),'Click to view AMQP/iNexus/IIB/OTESB connections st')]").click()

#driver.find_element(By.LINK_TEXT, "Click to view AMQP/i").click()
time.sleep(5)

driver.close()


