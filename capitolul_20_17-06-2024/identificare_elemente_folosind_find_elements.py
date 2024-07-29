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
butoane_tip_card = chrome_driver.find_elements(By.CSS_SELECTOR, '.card.mt-4.top-card')
# print(type(butoane_tip_card))
# print(len(butoane_tip_card))
# print(butoane_tip_card)


"""
1. Afisam in consola urmatoarea sintaxa: "Am identificat in pagina {url pagina} un numar de {nr_butoane} butoane de tip card"
2. Dam click pe cardul de tip interactiuni (Interactions) folosind metoda find elements si indexarea din lista de elemente
3. Navigam inapoi in pagina
4.Dam din nou click pe cardul de tip interactiuni folosind un XPATH pentru acesta
5. Inchidem sesiunea curenta
"""
print(f"Am indentificat in pagina {chrome_driver.current_url} un numar de {len(butoane_tip_card)} butoane de tip card")
# butoane_tip_card[4].click()
# time.sleep(2)
chrome_driver.back()
time.sleep(2)
#4
chrome_driver.find_element(By.XPATH, "//h5[text()='Interactions']").click()
time.sleep(2)
#
# chrome_driver.back()
# time.sleep(2)
#5
chrome_driver.quit()
