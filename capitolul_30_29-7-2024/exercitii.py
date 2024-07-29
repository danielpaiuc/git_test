"""
1. Navigati pe urmatorul URL : https://www.wtatennis.com/
2. Apasati pe tab-ul 'Rankings'
3. Filter by Region -> Romania
4. Apasati pe 'Age' pentru a filtra rezultatele in mod crescator in functie de varsta
5. Selectati in formatul urmator de mai jos primele 10 jucatoare de tenis cu varsta cuprinsa intre 19 si 23 de ani:
1. Nume_prenume - Rank
2. Nume_prenume - Rank
3. Nume_prenume - Rank

si scriele intr-un fisier .txt in care poti sa pui header-ul sub forma
Player Name - Age
"""

import time
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WtaRankings(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.wtatennis.com/")
        self.chrome_driver.implicitly_wait(5)

    def close_advertisment(self):
        x_button = self.chrome_driver.find_element(By.XPATH, "//div[@class='splash-screen__front']//button[@class='close-button js-close']")
        x_button.click()


    def accept_cookies(self):
        ac_button = self.chrome_driver.find_element(By.XPATH, "//button[@data-text='Accept Cookies']")
        ac_button.click()

    def close_session(self):
        time.sleep(5)
        self.chrome_driver.quit()

    def rankings(self):
        rank_button = self.chrome_driver.find_element(By.XPATH, "//li[@class='main-navigation__item    js-dynamic-child ']//a[@title='Rankings']")
        rank_button.click()
        all_reg_button = self.chrome_driver.find_element(By.XPATH, "//div[text()='All Regions']")
        all_reg_button.click()
        ro_btn = self.chrome_driver.find_element(By.XPATH, "//li[@id='opt-elem-ROU']")
        ro_btn.click()
        age_button = self.chrome_driver.find_element(By.XPATH, "//th[@data-sort='BirthDate']")
        age_button.click()

    def generate_player_list(self):
        player_list = self.chrome_driver.find_elements(By.XPATH, "//tr[@class='rankings__row js-player-item-favourite']//td[contains(@class, 'age')]")
        for index in range(len(player_list)):
            if int(self.chrome_driver.find_elements(By.XPATH, "//td[@class='rankings__cell rankings__cell--age']")[index].text) >= 19:
                print(self.chrome_driver.find_elements(By.XPATH, "//td[@class='rankings__cell rankings__cell--player']//a")[index].text + " " + self.chrome_driver.find_elements(By.XPATH, "//td[@class='rankings__cell rankings__cell--age']")[index].text)


i1 = WtaRankings()
i1.close_advertisment()
i1.accept_cookies()
i1.rankings()
i1.generate_player_list()
i1.close_session()