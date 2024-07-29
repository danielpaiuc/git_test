"""
Test Afisare viteza de download si upload a conexiunii dumneavoastra la internet
1. Navigati pe site-ul "https://www.speedtest.net/"
2. Apasati butonul de accept cookies
3. Apasati butonul 'I Accept' pentru a incepe testul
4. Asteptati pana cand testul de download cat si testul de download sunt efectuate cu succes
5. Apasati pe butonul 'Back to test results'
6. Afisati in consola viteza de download sub forma: "Your download speed is {download_speed}"
7. Afisati in consola viteza de upload sub forma: "Your upload speed is {upload_speed}"
8. Inchideti sesiunea
"""


import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTest(CommonMethods):

    #TEXT_BASED_BTN = "//button[text()='{}']"


    def __init__(self):
        super().__init__()
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.speedtest.net/")
        self.chrome_driver.implicitly_wait(2)


    def acc_cookies(self):
        cookies_button = self.chrome_driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        cookies_button.click()

    def click_go_button(self):
        go_button = self.chrome_driver.find_element(By.XPATH, "//span[text()='Go']")
        go_button.click()
        WebDriverWait(self.chrome_driver, 45).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Result ID']")))

    def display_speed(self):
        self.download_speed = self.chrome_driver.find_element(By.XPATH, "//span[contains(@class, 'download-speed')]").text
        self.upload_speed = self.chrome_driver.find_element(By.XPATH, "//span[contains(@class, 'upload-speed')]").text
        print(f"Your download speed is {self.download_speed} Mb/s")
        print(f"Your upload speed is {self.upload_speed} Mb/s")

    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = InternetSpeedTest()
i1.acc_cookies()
i1.click_go_button()
i1.display_speed()
i1.close_session()
