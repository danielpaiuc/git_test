"""
1) Navigati pe site-ul de https://www.flanco.ro/

2) Apasati pe butonul de Accept Cookies

3) Apasati pe 'Alegere Categoria'

4) Apasati pe 'Electrocasnice Bucatarie'

5) Apasati pe 'Cuptoare Microunde si Electrice'

6) Apasati pe 'Cuptoare Electrice'

7) Aplicam filtrul de 'Capacitate' cu valoarea intre 31 l - 40 l

8) Aplicam filtrul de 'Pret' cu valoare 400, 00 - 499,99 RON

9) Sortam rezultatele dupa 'Pret Descendent'

10) Afisam in consola descrierea produsului(partea cu bold de pe site) si pretul acestuia sub forma:

Cel mai scump cuptor electric cu o capacitate cuprinsa intre 31 l si 40l, cu un pret intre 400 si 500 RON este
Cuptor electric cu convectie Zass ZEO 38 CR, 1600 W, 38 l, Grill, Rotisor cu pretul de PRET_PRODUS
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import gettext

class Flanco:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.flanco.ro/")


    def close_session(self):
        self.chrome_driver.quit()

    def accept_cookies(self):
        a = self.chrome_driver.find_element(By.XPATH, "//a[text()='Permite toate']")
        a.click()


    def choose_category(self):
        b = self.chrome_driver.find_element(By.XPATH, "//button[@title='Toggling menu']")
        b.click()

    def choose_electrocasnice_bucatarie(self):
        c = self.chrome_driver.find_element(By.XPATH, "//figure[@title='Toggle item Electrocasnice Bucatarie']")
        c.click()

    def choose_cuptoare_electrice(self):
        d = self.chrome_driver.find_element(By.XPATH, "//span[text()='Cuptoare Electrice']")
        d.click()

    def optiune_capacitate(self):
        e = self.chrome_driver.find_element(By.XPATH, '//span[text()="31  l - 40  l"]')
        e.click()

    def interval_pret(self):
        f = self.chrome_driver.find_element(By.XPATH, '//span[text()="400,"]')
        f.click()

    def sortare_pret_descendent(self):
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@class='sorter-options']"))
        dropdown.select_by_visible_text("Pret Descendent")

    def printare_descriere(self):
        most_expensive_prod_description = self.chrome_driver.find_elements(By.XPATH, "//strong[contains(@class,'product-item-name')]//a//h2")[0].text
        most_expensive_prod_price_w_currency = self.chrome_driver.find_elements(By.XPATH, "//span[@class='special-price']//span[@class='price']")[0].text
        most_expensive_prod_price_value = float(most_expensive_prod_price_w_currency.split(" ")[0].replace(',', '.'))

        print(f"Cel mai scump cuptor electric cu o capacitate cuprinsa intre 31 l si 40l, cu un pret intre 400 si 500 RON este {most_expensive_prod_description} si are pretul {most_expensive_prod_price_value} RON")

    def execute_test(self):
        self.accept_cookies()
        time.sleep(2)
        self.choose_category()
        time.sleep(2)
        self.choose_electrocasnice_bucatarie()
        time.sleep(2)
        self.choose_cuptoare_electrice()
        time.sleep(2)
        self.optiune_capacitate()
        time.sleep(2)
        self.interval_pret()
        time.sleep(2)
        self.sortare_pret_descendent()
        time.sleep(2)
        self.printare_descriere()
        time.sleep(2)
        self.close_session()

f1 = Flanco()
f1.execute_test()


