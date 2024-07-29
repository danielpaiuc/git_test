"""
1. Navigati pe adresa https://testpages.eviltester.com/styled/canvas-javascript-test.html
2. Apasati pe butonul 'Clear' pentru a sterge continul din patratul care reprezinta plansa de desenare
3. Completati patratul cu 9 patrate cu latura de 100 pixeli fiecare, pornind de la x = 0 si y = 0, tinand cont
ca fiecare patrat trebuie sa aiba o culoare random
4. Inchideti sesiunea
"""

import time
import random
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class ColoringSquare(CommonMethods):
    X = [0, 100, 200]
    Y = [0, 100, 200]

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testpages.eviltester.com/styled/canvas-javascript-test.html")
        self.chrome_driver.implicitly_wait(5)

    def clear_square(self):
        clear_button = self.chrome_driver.find_element(By.XPATH, "//input[@name='clearbutton']")
        clear_button.click()

    def select_square_shape(self):
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='shapeselect']"))
        dropdown.select_by_value("0")

    def select_mini_square_color(self):
        color_list = ["#000000", "#FF0000", "#00FF00", "#0000FF", "#C0C0C0"]
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='colourselect']"))
        dropdown.select_by_value(random.choice(color_list))

    def mini_square_size(self):
        square_size = self.chrome_driver.find_element(By.XPATH, "//input[@name='shapesize']")
        square_size.clear()
        square_size.send_keys("100")

    def show_mini_square(self):
        show_button = self.chrome_driver.find_element(By.XPATH, "//input[@name='gobutton']")
        show_button.click()

    def fill_square(self):
        horizontal_btn = self.chrome_driver.find_element(By.ID, "xnum")
        vertical_btn = self.chrome_driver.find_element(By.ID, "ynum")
        for horizontal in ColoringSquare.X:
            for vertical in ColoringSquare.Y:
                horizontal_btn.clear()

                horizontal_btn.send_keys(str(horizontal))
                vertical_btn.clear()

                vertical_btn.send_keys(str(vertical))

                self.select_mini_square_color()
                self.show_mini_square()

    def close_session(self):
        time.sleep(5)
        self.chrome_driver.quit()


i1 = ColoringSquare()
i1.clear_square()
i1.mini_square_size()
i1.select_square_shape()
i1.fill_square()
i1.close_session()
