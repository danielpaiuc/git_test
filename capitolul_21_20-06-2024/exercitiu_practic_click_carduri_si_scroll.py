import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
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
time.sleep(4)
chrome_driver.get(url="https://demoqa.com/")
butoane_tip_card = chrome_driver.find_elements(By.CSS_SELECTOR, ".card.mt-4.top-card")

"""
Sa se foloseasca o bucla for pentru a da click pe fiecare card/buton din lista butoane_tip_card
iar dupa fiecare click sa se navigheze inapoi in pagina, iar unde este nevoie, folosim metoda 
scroll
"""

def scroll_x_y_axis_by_value(x_axiss_scroll_value=0, y_axis_scroll_value=0):
    chrome_driver.execute_script(f'window.scrollBy({x_axiss_scroll_value}, {y_axis_scroll_value});')
    time.sleep(1)

keep_scrolling = True
for i in range(len(butoane_tip_card)):
    while keep_scrolling:
        try:
            butoane_tip_card = chrome_driver.find_elements(By.CSS_SELECTOR, ".card.mt-4.top-card")
            butoane_tip_card[i].click()
            time.sleep(1)
            chrome_driver.back()
            time.sleep(1)
            break
        except ElementClickInterceptedException:
            scroll_x_y_axis_by_value(y_axis_scroll_value=100)





