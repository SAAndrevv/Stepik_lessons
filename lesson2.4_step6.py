#!/usr/bin/python

from selenium import webdriver

link = r"http://suninjuly.github.io/cats.html"

browser = webdriver.Chrome()

browser.implicitly_wait(5)

browser.get(link)

browser.find_element_by_id("button")


