"""
1. Navigam pe site-ul python.org
2. Maximizam fereastra de lucru
3. a) Vrem sa apasam pe butonul de "Go"
"""


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(executable_path= r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

# 1 1. Navigam pe site-ul python.org
chrome_driver.get(url="https://python.org")
# 2. Maximizam fereastra de lucru
chrome_driver.maximize_window()
time.sleep(4)
# 3 a) Vrem sa apasam pe butonul de "Go" (ne folosim de ID)

go_button_by_ID = chrome_driver.find_element(By.ID, "submit")
print("Am identificat butonul go utilizand ID-ul acestuia")
print("Clicking go button")
go_button_by_ID .click()
time.sleep(3)

print("Navigam inapoi")
chrome_driver.back() # goes 1 step backwards in the browser history
time.sleep(3)

go_button_by_name = chrome_driver.find_element(By.NAME, "submit")
print("Am identificat butonul go utilizand numele acestuia")
print("Clicking go button")
go_button_by_ID .click()
time.sleep(5)
chrome_driver.close()