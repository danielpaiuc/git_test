"""
Fizz buzz exercitiu.

"""

import time
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class FizzBuzz(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://jenniferdewalt.com/fizz_buzz.html")
        self.chrome_driver.implicitly_wait(5)

    def start_the_game(self):
        start_button = self.chrome_driver.find_element(By.XPATH, "//input[@class='btn start']")
        start_button.click()

    def fizz_buzz_rules(self):
        current_number = int(self.chrome_driver.find_element(By.XPATH, "//div[@class='cur_num']").text)
        text_to_be_entered = self.chrome_driver.find_element(By.XPATH, "//input[@class='text']")
        enter_button = self.chrome_driver.find_element(By.XPATH, "//input[@class='btn enter']")
        if current_number % 3 == 0 and current_number % 5 == 0:
            text_to_be_entered.send_keys("fizz buzz")
        elif current_number % 5 == 0:
            text_to_be_entered.send_keys("buzz")
        elif current_number % 3 == 0:
            text_to_be_entered.send_keys("fizz")
        else:
            text_to_be_entered.send_keys(f"{current_number}")
        enter_button.click()

    def iterate_rounds_left(self):
        rounds_left_text = self.chrome_driver.find_element(By.XPATH, "//div[@class='stat count']").text
        rounds_left = int(rounds_left_text[13:])
        while rounds_left != 0:
            self.fizz_buzz_rules()
            rounds_left -= 1

    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = FizzBuzz()
i1.start_the_game()
i1.iterate_rounds_left()

i1.close_session()
