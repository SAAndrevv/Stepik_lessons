#!/usr/bin/python

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, text)
    button.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

