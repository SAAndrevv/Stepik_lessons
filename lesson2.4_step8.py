#!/usr/bin/python

import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = r"http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()

finally:
    
    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(10)
    alert.accept()
    time.sleep(5)
    browser.quit()

