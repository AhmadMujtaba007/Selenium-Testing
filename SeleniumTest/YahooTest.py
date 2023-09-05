from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
# Yahoo credentials
# username = "am_191203"
# password = "HelloYahoo1"
# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to Yahoo login page
# I have used a link shortener because Original yahoo login link was too large
driver.get("http://127.0.0.1:5000") # localhost
# find username/email field and send the username itself to the input field
# driver.find_element("name", "username").send_keys(username)
# click Next button
# driver.find_element("name", "signin").click()

time.sleep(100)


# error_message = "Sorry, we don't recognize this email."
# # get the errors (if there are)
# errors = driver.find_elements(By.CLASS_NAME, "error-msg")

WebDriverWait(driver=driver, timeout=5).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
#     driver.close()
#     exit()


time.sleep(500)


# # find password input field and insert password as well
# driver.find_element("name", "password").send_keys(password)
# # click Next button again to login
# driver.find_element("name", "verifyPassword").click()


# error_message = "Invalid password. Please try again"
# # get the errors (if there are)
# errors = driver.find_elements(By.CLASS_NAME, "error-msg")

# WebDriverWait(driver=driver, timeout=5).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )

# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")

# close the driver
driver.close()
