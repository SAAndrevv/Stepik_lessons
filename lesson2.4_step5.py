#!/usr/bin/python

from selenium import webdriver 
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(5)

try:
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.find_element(By.ID, "verify").click()

    message = browser.find_element(By.ID, "verify_message").text

finally:

    assert "successful" in message, "No elements"
    browser.quit()



