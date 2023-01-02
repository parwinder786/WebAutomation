from selenium import webdriver

browser = webdriver.Edge(r"C:\Users\XT23495\Downloads\Driver_Notes\msedgedriver.exe")

browser.get('https://www.google.com/?safe=active&ssui=on')

browser.close()


