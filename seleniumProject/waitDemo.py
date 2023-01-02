
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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


#pause the test for few seconds using Time class

driver.implicitly_wait(5)  # Global timeout
# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3   # to check if the count is 3

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    #actualList.append(button.find_element(By.XPATH, "h4").text) # append method gonna add items into the list
    button.click()

#print(actualList)
#assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prcies = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prcies:
    price.text # looping tthrough lisrt
    sum = sum + int(price.text)    # adding the sum of all eleements
print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) #it will be string

assert sum == total_amount


driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
#wait.until() #untill up to what time/condition  u want to wait , it resumes once elements find, wait apply to specified element
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
driver.close()
