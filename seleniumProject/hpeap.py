
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver

try:
    #driver = webdriver.Chrome(executable_path="C:\\Users\\XT23495\\Downloads\\chromeDriver\\chromedriver.exe")
    driver = webdriver.Edge(r"C:\Users\XT23495\Downloads\Driver_Notes\msedgedriver.exe")


    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("https://10.249.24.150:43443/PowerViewInterface.shtml")

    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()


    time.sleep(10)
    cd  = driver.find_elements(By.TAG_NAME, "iframe").__sizeof__()
    print(cd)
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='main_banner']"))
    driver.find_element(By.XPATH, "//a[@id='diag']").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, "//body/iframe[3]"))

    ab = driver.find_element(By.XPATH, "//div[contains(text(),'SSD Size:')]").text
    #gg = driver.find_element(By.XPATH, "//div[@id='DivSSDSize']").text
    time.sleep(10)
    #gg = driver.find_element(By.XPATH, "//div[contains(text(),'SSD Size:')]").get_attribute('value')
    gg = driver.find_element(By.CSS_SELECTOR,"#DivSSDSize").text


    print(ab)
    print(gg)
    var = '2TB'
    if gg == var:
        print(' the SSD size of memory is as expected = ' + gg)
    else:
        print('the SSD size of memory is not as expected = '+ gg)
except NoSuchElementException as e:
    print(e)
