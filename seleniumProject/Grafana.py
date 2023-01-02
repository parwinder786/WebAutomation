from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\\Users\\XT23495\\Downloads\\chromedriver.exe");
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# ID, Xpath, CSS selector , Class name , name & link test

# xpath //tagname[@attribute='value']  //button[@aria-label='Login button']
# CSS tagname[attribute='value']   #id will be css  .classname will also css
# link text will identify if HTML has anchor link

driver.get("http://mtl-xb1d-01m:8080/login")
driver.find_element(By.NAME, "user").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("itcmep0")
#driver.find_element(By.CLASS_NAME, "css-1daj7gy-button").click()
# for radio button its click option



driver.find_element(By.XPATH, "//button[@aria-label='Login button']").click()
time.sleep(10)
driver.find_element(By.XPATH, "//body/grafana-app[1]/div[1]/div[1]/react-container[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/a[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//body/grafana-app[1]/div[1]/div[1]/react-container[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/button[1]/span[2]/div[1]").click()

driver.find_element(By.XPATH, "//span[contains(text(),'Last 5 minutes')]").click()

#select class for static drop down
#dropdown = Select(driver.find_element(By.XPATH, "//span[contains(text(),'Last 24 hours')]"))
#ther are many method select - by index, by visible text, or value
#dropdown.select_by_index(1)
#dropdown.select_by_visible_text("Last 5 minutes")

#driver.find_element(By.LINK_TEXT, "ITCM XB1").click()

#print(msg)
print(driver.title)
time.sleep(10)
driver.close()
