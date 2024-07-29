"""
1. Navigati pe site-ul https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html
2. Selectati din dropdown-ul 'Course Name', la intamplare(folosim random) , una din urmatoarele 3 optiuni de limbaje de programare:
Java, Python, JavaScript
3. Selectati din dropdown-ul cu multiple values 'IDE Name', urmatoarele IDE-uri:
3.1) Ultimele 3 IDE-uri iar
3.2) Deselectati toate IDE-urile si selectati IDE-ul al carui nume contine cele mai multe vocale
"""

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class Selectare:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

    def close_session(self):
        self.chrome_driver.quit()

    def select_value(self):

        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='course']"))
        time.sleep(3)
        index_list = [1, 3, 4]
        index = random.choice(index_list)
        dropdown.select_by_index(index)

    def select_value_2(self):
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='ide']"))
        time.sleep(2)
        dropdown.select_by_value("ij")
        time.sleep(2)
        dropdown.select_by_value("vs")
        time.sleep(2)
        dropdown.select_by_value("nb")
        time.sleep(2)

    def accept_cookies(self):
        a = self.chrome_driver.find_element(By.XPATH, "//p[text()='Consent']")
        a.click()

    def deselect_all(self):
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='ide']"))
        dropdown.deselect_all()

    def vowel_selection(self):
        dropdown = Select(self.chrome_driver.find_element(By.XPATH, "//select[@id='ide']"))
        text_list = ['Eclipse', 'IntelliJ IDEA', 'Visual Studio', 'NetBeans']
        maximum = 0
        most_vowels_string = ''
        for i in range(len(text_list)):
            counter = 0
            for character in text_list[i].lower():

                if character in "aeiou":
                    counter += 1
            if counter > maximum:
                maximum = counter
                most_vowels_string = text_list[i]
        dropdown.select_by_visible_text(most_vowels_string)


i1 = Selectare()
time.sleep(2)
i1.accept_cookies()
time.sleep(2)
i1.select_value()
time.sleep(2)
i1.select_value_2()
time.sleep(2)
i1.deselect_all()
time.sleep(3)
i1.vowel_selection()
time.sleep(3)
i1.close_session()
