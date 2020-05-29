#!/usr/bin/python

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("example")
    browser.find_element(By.NAME, "lastname").send_keys("example")
    browser.find_element(By.NAME, "email").send_keys("example")

    path_file = os.path.abspath(os.path.dirname(__file__))
    send_file = os.path.join(path_file, "fle.txt")

    browser.find_element(By.ID, "file").send_keys(send_file)

    browser.find_element(By.TAG_NAME, "button").click()

finally:

    time.sleep(10)
    browser.quit()

