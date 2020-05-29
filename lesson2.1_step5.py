#!/usr/bin/python

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    
    time.sleep(15)
    browser.quit()




