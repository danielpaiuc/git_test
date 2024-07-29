"""
Creati urmatoarele doua metode in clasa InteractiuneRadioButtonsPlusCheckboxuri de mai jos:

1) Metoda enable_radio_buttons care va activa pe rand cele trei radio button-uri disponibile.

Pentru acest punct trebuie sa folosim o bucla for si localizarea celor trei butoane sa se faca dupa atributul for care
va fi de tipul gender-ratio-1, gender-ratio-2 si gender-ratio-3. Nu folosim metoda find elements ci folosim un locator
care sa varieze in functie de 1, 2, 3.

2) Metoda enable_checkboxes care sa selecteze pe rand cele trei checbox-uri disponibile.De asemenea, se cere sa nu se
foloseasca metoda find_elements ci o bucla for in care sa folosim un locator variabil dupa hobbies-checkbox-1, 2 sau 3.

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class InteractiuneRadioButtonsPlusCheckboxuri:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://demoqa.com/automation-practice-form")
        time.sleep(2)

    def close_session(self):
        self.chrome_driver.quit()

    def enable_radio_buttons(self):
        for i in range(1, 4):
            radio_btn = self.chrome_driver.find_element(By.XPATH, f"//label[@for='gender-radio-{i}']")
            radio_btn.click()
            time.sleep(2)

    def enable_checkbox_buttons(self):
        for i in range(1, 4):
            checkbox_btn = self.chrome_driver.find_element(By.XPATH, f"//label[@for='hobbies-checkbox-{i}']")
            checkbox_btn.click()
            time.sleep(2)


i1 = InteractiuneRadioButtonsPlusCheckboxuri()
i1.enable_radio_buttons()
time.sleep(2)
i1.enable_checkbox_buttons()

