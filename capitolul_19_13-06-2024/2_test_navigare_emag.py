import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(executable_path= r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

chrome_driver.get(url="https://emag.ro")
time.sleep(1)
chrome_driver.maximize_window()

"""
Atunci cand identificam elementel dupa selectorii CSS, folosim urmatoarele:
. -> pentru identificarea dupa clasa (.className)
# -> pentru identificarea dupa ID (#userName)
"""

"""
Identificati butonul de accept cookies in urm moduri:

1. dupa xpath
//title[@lang='en']

2. dupa selectorul css
3. dupa class name
4. dupa xpath cu metoda de text

"""

# 1. Dupa XPATH
# time.sleep(2)
# accept_cookies_by_xpath = chrome_driver.find_element(By.XPATH, "//button[@class='btn btn-primary js-accept gtm_h76e8zjgoo btn-block']")
# accept_cookies_by_xpath.click()
# time.sleep(2)
# 2. Dupa selectorul CSS
# time.sleep(2)
# accept_cookies_by_css = chrome_driver.find_element(By.CSS_SELECTOR, ".js-accept")
# accept_cookies_by_css.click()
# time.sleep(2)
# # 3. Dupa class name

# time.sleep(2)
# accept_cookies_by_class_name = chrome_driver.find_element(By.CLASS_NAME, 'js-accept')
# accept_cookies_by_class_name.click()
# time.sleep(2)
# # 4. Dupa xPath dar folosind si metoda de text()
#

time.sleep(2)
accept_cookies_by_xpath_with_text = chrome_driver.find_element(By.XPATH, "//button[text()='Accept toate ']")
accept_cookies_by_xpath_with_text.click()
time.sleep(2)