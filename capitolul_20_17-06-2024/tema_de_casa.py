import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(
    executable_path=r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

chrome_driver.maximize_window()
time.sleep(2)

chrome_driver.get(url="https://www.linkedin.com")
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//button[@action-type='ACCEPT']").click()
time.sleep(2)
email_or_phone = chrome_driver.find_element(By.ID, "session_key")
email_or_phone.send_keys("nume.prenume@gmail.com")
time.sleep(2)
password = chrome_driver.find_element(By.ID, "session_password")
password.send_keys("Parola4%")
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//button[@data-tracking-control-name='homepage-basic_sign-in-submit-btn']").click()


"""
//button[@action-type='ACCEPT']
//button[@data-tracking-control-name='homepage-basic_sign-in-submit-btn']
"""