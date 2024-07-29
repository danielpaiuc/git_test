"""
1. Navigati pe site-ul https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407
2. Completati campurile First Name, Last Name, Phone, Country, City, Email Address, Gender
3. Selectati 2 zile la intamplare(folositi random sau ce doriti si va asigurati ca zilele sunt diferite, in
felul asta evitand sa bifam si apoi sa debifam aceeasi zi)
4. Selectati din dropdown-ul Best Time to Contact una din optiuni.
5. Apasati pe submit.

"""

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Formular:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", False)
        self.chrome_driver = webdriver.Chrome()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

    def fill_in_data(self):
        first_name = self.chrome_driver.find_element(By.ID, "RESULT_TextField-1")
        first_name.send_keys("Daniel")
        time.sleep(2)

        last_name = self.chrome_driver.find_element(By.ID, "RESULT_TextField-2")
        last_name.send_keys("Paiuc")
        time.sleep(2)

        phone_number = self.chrome_driver.find_element(By.ID, "RESULT_TextField-3")
        phone_number.send_keys("0734046143")
        time.sleep(2)

        country = self.chrome_driver.find_element(By.ID, "RESULT_TextField-4")
        country.send_keys("Romania")
        time.sleep(2)

        city = self.chrome_driver.find_element(By.ID, "RESULT_TextField-5")
        city.send_keys("Bucharest")
        time.sleep(2)

        email = self.chrome_driver.find_element(By.ID, "RESULT_TextField-6")
        email.send_keys("paiucdaniel@gmail.com")
        time.sleep(2)

        gender = self.chrome_driver.find_element(By.XPATH, '//label[@for="RESULT_RadioButton-7_0"]')
        gender.click()
        time.sleep(2)

    def select_days(self, no_days):
        day_indices = [0, 1, 2, 3, 4, 5, 6]
        for i in range(no_days):
            k = random.choice(day_indices)
            selected_day = self.chrome_driver.find_element(By.XPATH, f'//label[@for="RESULT_CheckBox-8_{k}"]')
            selected_day.click()
            day_indices.remove(k)
            time.sleep(1)
        time.sleep(2)

    def select_time_to_contact(self):
        dropdown = Select(self.chrome_driver.find_element(By.ID, "RESULT_RadioButton-9"))
        time.sleep(2)
        time_list = ["Radio-0", "Radio-1", "Radio-2"]
        dropdown.select_by_value(random.choice(time_list))
        time.sleep(2)

    def press_submit(self):
        submit = self.chrome_driver.find_element(By.ID, "FSsubmit")
        submit.click()
        time.sleep(2)

    def close_session(self):
        self.chrome_driver.quit()


f1 = Formular()
f1.fill_in_data()
f1.select_days(2)
f1.select_time_to_contact()
f1.press_submit()
f1.close_session()
