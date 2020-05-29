#!/usr/bin/python

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = r"http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    inp_val = browser.find_element(By.ID, "input_value")
    x = inp_val.text
    y = calc(x)

    inp_text = browser.find_element(By.ID, "answer")
    inp_text.send_keys(y)

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    
    answer = browser.switch_to.alert
    alert_text = answer.text
    print(alert_text)
    time.sleep(5)
    browser.quit()


