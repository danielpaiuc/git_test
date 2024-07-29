"""
1) Navigati pe site-ul https://www.gigacalculator.com/calculators/leap-year-calculator.php
2) Bifati 'All leap years between two years' pentru campul Calculate
3) Introduceti pentru campul 'Start year' o valoare random intre 1600 si 1650
4) Introduceti pentru campul 'End year' o valoare random intre 1975 si 2480
5) Apasat pe butonul 'Calculate'
6) Afisati in consola urmatoarea fraza: 'Numarul de ani bisecti cuprinsi intre <start_year> si <end_year> este de <numar_ani_bisecti>.'
7) Stocati intr-o lista toti anii bisecti afisati in sectiunea 'Calculation results' a site-ului
"""

"""
1) Creati un program care sa calculeze numarul de ani bisecti folosind valorile de la primul program
2) Verificati daca numarul total de ani bisecti gasiti este identific cu cel din primul program
3) Validati ca au fost gasiti aceeasi ani bisecti
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.keys import Keys


class AnBisect(CommonMethods):
    START_YEAR = str(random.choice(list(range(1600, 1651))))
    END_YEAR = str(random.choice(list(range(1975, 2481))))

    def __init__(self):
        super().__init__()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.gigacalculator.com/calculators/leap-year-calculator.php")

    def close_session(self):
        self.chrome_driver.quit()

    def accept_cookies(self):
        a = self.chrome_driver.find_element(By.XPATH, "//span[text()='AGREE']")
        a.click()

    def check_all_leap_years_btw_2(self):
        b = self.chrome_driver.find_element(By.XPATH, "//label[@for='solve2']")
        b.click()
        time.sleep(2)

    def fill_start_year(self):
        start_year = self.chrome_driver.find_element(By.XPATH, '//input[@id="year1"]')
        start_year.send_keys(self.START_YEAR)
        time.sleep(2)

    def fill_end_year(self):
        end_year = self.chrome_driver.find_element(By.XPATH, '//input[@id="year2"]')
        end_year.send_keys(self.END_YEAR)
        time.sleep(2)

    def calculate_leap_year(self):
        c = self.chrome_driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-lg"]')
        c.click()
        time.sleep(2)

    def display_leap_years(self):
        print(
            f"Numarul de ani bisecti intre {self.START_YEAR} and {self.END_YEAR} este {self.chrome_driver.find_element(By.XPATH, "//th[@scope='row']").text}")
        time.sleep(2)


ab1 = AnBisect()
ab1.accept_cookies()
ab1.check_all_leap_years_btw_2()
ab1.fill_start_year()
ab1.fill_end_year()
ab1.calculate_leap_year()
ab1.display_leap_years()
ab1.close_session()
