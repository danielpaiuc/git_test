"""
1. Navigam pe https://www.booking.com/
2. Apasam pe butonul de 'Accept cookies'
3. Ne cream o metoda care sa ne returneze daca butonul de valuta (RON, EUR, USD, etc.) este vizibil pe pagina sau nu urmand pasii:
3.1.Verificam daca butonul este vizibil pe pagina si afisam in consola "Butonul de valuta este vizibil in pagina"
3.2 Aplicam pentru acest buton un atribut pentru a nu mai fi vizibil pe pagina(hidden)
3.3.Verificam ca butonul de valuta nu mai este vizibil pe pagina si afisam in consola "Butonul de valuta nu este vizibil in pagina"
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from automation.CommonMethods import CommonMethods


class BookingAscuns(CommonMethods):
    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.booking.com/")

    def accept_cookies(self):
        a = self.chrome_driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        a.click()

    def close_session(self):
        self.chrome_driver.quit()

locator = "//span[text()='RON']"
b1 = BookingAscuns()
time.sleep(2)
b1.accept_cookies()
time.sleep(2)
if b1.check_visibility(locator) == True:
    print("Butonul de valuta este vizibil in pagina")
else:
    print("Butonul de valuta nu este vizibil in pagina")
b1.hide_specific_element("//span[text()='RON']")
time.sleep(3)
print(b1.check_visibility(locator))
time.sleep(3)
