from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


service_obj = Service("C:\\Users\\XT23495\\Downloads\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


checkboxes = driver.find_elements(by=By.XPATH, value="//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
driver.close()

# radiobuttons = driver.find_elements_by_name("radioButton")
# radiobuttons[2].click()
# assert radiobuttons[2].is_selected()
#
# assert driver.find_element_by_id("displayed-text").is_displayed()
#
# driver.find_element_by_id("hide-textbox").click()
#
# assert not driver.find_element_by_id("displayed-text").is_displayed()