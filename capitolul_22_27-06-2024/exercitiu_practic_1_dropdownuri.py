"""
Navigati pe site-ul https://testautomationpractice.blogspot.com/
Selectati din dropdown-ul afisat urmatoarele:
2.1) Selectati "France" folosind index-ul
2.2) Selectati "Brazil folosind valoarea
2.3) Selectati "Australia" folosind textul campului
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class Selectare:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testautomationpractice.blogspot.com/")


    def close_session(self):
        self.chrome_driver.quit()

    def select_value(self):

        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='country']"))
        time.sleep(3)
        dropdown.select_by_index(4)
        time.sleep(3)
        dropdown.select_by_value("brazil")
        time.sleep(3)
        dropdown.select_by_visible_text("Australia")
        time.sleep(3)



i1 = Selectare()
i1.select_value()
i1.close_session()
