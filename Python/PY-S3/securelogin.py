from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("your login url") 
time.sleep(10)
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("username")
password.send_keys("password")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
