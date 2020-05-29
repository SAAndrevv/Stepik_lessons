#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = r"http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    amount = int(num1) + int(num2)
    amount = str(amount)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(amount)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    print(browser.switch_to.alert.text)
    time.sleep(15)
    browser.quit()

    

