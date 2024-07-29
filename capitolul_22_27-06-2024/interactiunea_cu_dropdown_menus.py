import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class SelectareDropDownElement:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testpages.eviltester.com/styled/basic-html-form-test.html")

    def select_dropdown_element(self):
        print("A")
        dropdown_menu = Select(self.chrome_driver.find_element(By.XPATH, "//select[@name='dropdown']"))
        print("A")

        # Exercitiu - selectam din dropdown menu diferite optiuni

        # 1) Selectare dupa valoare (dupa valoarea atributului value)
        time.sleep(3)
        dropdown_menu.select_by_value("dd6")
        time.sleep(3)
        # 2) Selectare dupa indexul elementului (din dropdown cautat)
        dropdown_menu.select_by_index(1)  # index 1 e optiunea a 2 a
        time.sleep(3)
        # 3) Selectare dupa textul elementului din dropdown
        dropdown_menu.select_by_visible_text("Drop Down Item 4")
        time.sleep(3)

    def close_session(self):
        self.chrome_driver.quit()


i1 = SelectareDropDownElement()
i1.select_dropdown_element()
i1.close_session()
