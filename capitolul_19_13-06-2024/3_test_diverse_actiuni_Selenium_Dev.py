"""
1. Navigam pe site-ul https://www.selenium.dev/
2. Dam click pe butonul "Downloads"
3. Dam click pe butonul link-ul "other languages exist"
4. Dam un refresh la pagina
5. Afisam in consola titlul paginii curente in formatul urmator: "Titul paginii curente este: {titlul_paginii}"
6. Apasam pe back pentru a naviga catre pagina anterioara
7. Afisam in consola titlul paginii curente in formatul urmator: "Titul paginii curente este: {titlul_paginii}"
8. Apasam pe butonul de forward
9. Apasam butonul back de 2 ori pentru a naviga la pagina initiala
10. Afisam in consola titlul paginii curente in formatul urmator: "Titul paginii curente este: {titlul_paginii}"
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(
    executable_path=r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

chrome_driver.maximize_window()
# 1. Navigam pe site-ul https://www.selenium.dev/
chrome_driver.get(url="https://www.selenium.dev")

time.sleep(2)

# 2.

accept_cookies_by_xpath_with_text = chrome_driver.find_element(By.XPATH, "//span[text()='Downloads']")
accept_cookies_by_xpath_with_text.click()
time.sleep(2)
# 3

chrome_driver.find_element(By.XPATH, "//a[text()='other languages exist']").click()
time.sleep(2)

# 4

chrome_driver.refresh()
time.sleep(2)
# 5
print(f"Titul paginii curente este: {chrome_driver.title}")
# 6
chrome_driver.back()
time.sleep(2)
# 7
print(f"Titul paginii curente este: {chrome_driver.title}")
# 8
chrome_driver.forward()
time.sleep(2)
# 9
chrome_driver.back()
time.sleep(2)
chrome_driver.back()
time.sleep(2)
print(f"Titul paginii curente este: {chrome_driver.title}")
time.sleep(2)
chrome_driver.quit()
