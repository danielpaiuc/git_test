"""
Pornind de la URL-ul https://jenniferdewalt.com/dice_roller.html , afisati in consola suma numerelor afisate
pe cel de al doilea zar, pentru 10 aruncari de zar consecutive.
"""

import time
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DiceRoller(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://jenniferdewalt.com/dice_roller.html")
        self.chrome_driver.implicitly_wait(5)


    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()

    def read_second_dice_value(self):
        second_dice_value = len(self.chrome_driver.find_elements(By.XPATH, "//div[@id='die_2']/div[@style='display: block;']"))
        return second_dice_value

    def shake_dice(self):
        shakedem_button = self.chrome_driver.find_element(By.XPATH, "//div[@id='shaker']/div")
        shakedem_button.click()

    def second_dice_sum_by_iterations(self, no_dice_shakes):
        second_dice_sum = 0
        for counter in range(no_dice_shakes):
            log.info(f"Suntem la aruncarea cu numarul {counter+1}. Se arunca zarurile: ")
            self.shake_dice()
            WebDriverWait(self.chrome_driver, 2, poll_frequency=0.25).until(EC.invisibility_of_element((By.XPATH, "//h1[@class='shake']")))
            log.info(f"Al doilea zar are valoare de {self.read_second_dice_value()}")
            second_dice_sum += self.read_second_dice_value()
            log.info(f"Suma dupa aruncarea cu numarul {counter+1} pentru al doilea zar este {second_dice_sum}")


i1 = DiceRoller()
i1.second_dice_sum_by_iterations(10)

