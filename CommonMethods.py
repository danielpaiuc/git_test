import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





class CommonMethods:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()

    def check_visibility(self, elem):
        elem_to_verify = self.chrome_driver.find_element(By.XPATH, elem)

        if elem_to_verify.is_displayed():
            print("Elementul cautat este afisat pe pagina")
        else:
            print("Elementul cautat nu este afisat pe pagina")
        time.sleep(2)

    def hide_specific_element(self, elem):
        elem_to_hide = self.chrome_driver.find_element(By.XPATH, elem)
        self.chrome_driver.execute_script("arguments[0].setAttribute('hidden', 'true')", elem_to_hide)
        time.sleep(2)

    def scroll_x_y_axis_by_value(self, x_axis_scroll_value=0, y_axis_scroll_value=0):
        self.chrome_driver.execute_script(f"window.scrollBy({x_axis_scroll_value}, {y_axis_scroll_value});")
        time.sleep(1)
