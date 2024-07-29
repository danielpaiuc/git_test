import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class SelectareMultipla:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testpages.eviltester.com/styled/basic-html-form-test.html")


    def close_session(self):
        self.chrome_driver.quit()

    def select_multiple_values(self):
        print("A")
        multiple_values_dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@name='multipleselect[]']"))

        #1) Deselctam optiunile deja selectate
        #Var 1
        time.sleep(3)
        multiple_values_dropdown.deselect_all()
        #selectam prima valoare dupa value
        time.sleep(3)
        multiple_values_dropdown.select_by_value("ms1")
        time.sleep(3)
        multiple_values_dropdown.select_by_index(2)
        time.sleep(3)
        multiple_values_dropdown.select_by_visible_text("Selection Item 2")
        time.sleep(3)
        #5) Deselectam a 3 a valoare dupa value
        multiple_values_dropdown.deselect_by_value("ms3")
        time.sleep(3)
        multiple_values_dropdown.deselect_all()
        time.sleep(3)
        print("A")


i1 = SelectareMultipla()
i1.select_multiple_values()
i1.close_session()
