"""
1) navigam pe siteul demoqa
2) ne cream o metoda care sa apese pe butonul 'new tab'
3) schimbam focusul pe noul tab deschis
4) afisam textul in consola
5) inchidem sesiunea de lucru

"""



import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class SchimbareFereastraDeLucru:
    def __init__(self, url):
        self.url = url
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(self.url)
        time.sleep(1)

    def new_tab(self):
        a = self.chrome_driver.find_element(By.XPATH, "//button[@id='tabButton']")
        a.click()
        self.chrome_driver.switch_to.window(self.chrome_driver.window_handles[-1])

    def close_session(self):
        self.chrome_driver.quit()

    def print_text(self):
        print(self.chrome_driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text)


i1 = SchimbareFereastraDeLucru("https://demoqa.com/browser-windows")

time.sleep(2)
i1.new_tab()
time.sleep(2)
i1.print_text()
time.sleep(2)
i1.close_session()