import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from date_text_box_form import FORM_INFORMATION_DICT

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(
    executable_path=r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

chrome_driver.maximize_window()
time.sleep(2)

chrome_driver.get(url="https://demoqa.com")

"""
1. Navigam pe site-ul https://www.demoqa.com
2. Dam click pe "Elements"
3. Dam click pe "Text Box"
4. Completam cele 4 date necesare din formularul text box utilizand datele din fisierul date_text_box_form.py
5. Apasam pe butonul de Submit
"""

#2
time.sleep(1)
chrome_driver.find_element(By.XPATH, "//h5[text()='Elements']").click()
time.sleep(1)

#3
chrome_driver.find_element(By.XPATH, "//span[text()='Text Box']").click()
time.sleep(1)

#4
full_name_field = chrome_driver.find_element(By.ID, "userName")
full_name_field.send_keys(FORM_INFORMATION_DICT["Full name"])
time.sleep(1)
full_email_field = chrome_driver.find_element(By.ID, "userEmail")
full_email_field.send_keys(FORM_INFORMATION_DICT["email address"])
time.sleep(1)
full_current_address = chrome_driver.find_element(By.ID, "currentAddress")
full_current_address.send_keys(FORM_INFORMATION_DICT["adresa curenta"])
time.sleep(1)
full_permanent_address = chrome_driver.find_element(By.ID, "permanentAddress")
full_permanent_address.send_keys(FORM_INFORMATION_DICT["adresa permanenta"] + Keys.TAB + Keys.ENTER)
time.sleep(1)

submit_button = chrome_driver.find_element(By.ID, "submit")
submit_button.click()
#chrome_driver.quit()