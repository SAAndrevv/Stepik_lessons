#!/usr/bin/python

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 120);")

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
   
    assert True
    time.sleep(10)
    browser.quit()



