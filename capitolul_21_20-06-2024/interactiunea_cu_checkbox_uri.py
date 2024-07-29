import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class InteractiuneCheckbox:
    def __init__(self):
        self.chrome_options_object = Options()
        self.chrome_options_object.add_experimental_option("detach", True)
        self.service_object = Service(
            executable_path=r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
        self.chrome_driver = webdriver.Chrome(service=self.service_object, options=self.chrome_options_object)
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testpages.eviltester.com/styled/basic-html-form-test.html")

    def select_checkboxes_v1(self):
        checkboxes = self.chrome_driver.find_elements(By.XPATH, "//input[@name='checkboxes[]']")
        # pt a bifa toate 3 checkboxuri avem urm variante
        # v1 bifam primele 2 checkboxuri si in felul acesta o sa fie bifate toate 3 (al 3 lea bifat by default)
        time.sleep(2)
        checkboxes[0].click()
        time.sleep(2)
        checkboxes[1].click()
        time.sleep(2)

    def select_checkboxes_v2(self):
        checkboxes = self.chrome_driver.find_elements(By.XPATH, "//input[@name='checkboxes[]']")
        # v2 iteram prin lista de webelemente pt checkboxuri si le selectam pe fiecare in parte folosind o
        # bucla de tip for

        for checkbox in checkboxes:
            if checkbox.is_selected():
                continue
            else:
                time.sleep(2)
                checkbox.click()
                time.sleep(2)

    def select_checkboxes_v3(self):
        checkboxes = self.chrome_driver.find_elements(By.XPATH, "//input[@name='checkboxes[]']")
        # pt a treia varianta, deselectam a 3 a casuta deoarece e bifata by default si apoi le selectam pe toate 3 folosind un for
        time.sleep(2)
        checkboxes[-1].click()
        time.sleep(2)
        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(2)

    def close_session(self):
        self.chrome_driver.quit()


i1 = InteractiuneCheckbox()
i1.select_checkboxes_v1()
i1.select_checkboxes_v2()
i1.select_checkboxes_v3()