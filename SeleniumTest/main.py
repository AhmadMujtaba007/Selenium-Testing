from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.google.com/')
driver.find_element("name", "q").send_keys("Air University")
time.sleep(2)
driver.find_element("name", "btnK").send_keys(Keys.ENTER)
time.sleep(2)
driver.close()
print("sample test case successfully completed")
