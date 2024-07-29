import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class InteractiuneRadioButtons:

    def __init__(self):
        self.chrome_options_object = Options()
        self.chrome_options_object.add_experimental_option("detach", True)
        self.service_object = Service(executable_path=r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")
        self.chrome_driver = webdriver.Chrome(service=self.service_object, options=self.chrome_options_object)
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://demoqa.com/radio-button")