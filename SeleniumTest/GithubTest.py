from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# GitHub credentials
username = "191203@students.au.edu.pk"
password = "Hellogithub123"
# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to GitHub login page
driver.get("https://github.com/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "login_field").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button
driver.find_element("name", "commit").click()
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
# close the driver
driver.close()
