


import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log

class ExplicitlyWaitExample(CommonMethods):

    TEXT_BASED_BTN = "//button[text()='{}']"
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    def __init__(self):
        super().__init__()
        self.chrome_driver.maximize_window()
        log.info(f"Navigam catre adresa -> {self.URL}")
        self.chrome_driver.get(url=self.URL)
        self.chrome_driver.implicitly_wait(2)


    def first_explicitly_wait_example(self):
        #1) Click 'Remove' button
        remove_btn = self.chrome_driver.find_element(By.XPATH, self.TEXT_BASED_BTN.format("Remove"))
        remove_btn.click()

        # Wait for 'Add button' to be visible/enabled/clickable in the page

        WebDriverWait(self.chrome_driver, 4.28, 0.25).until(EC.presence_of_element_located((By.XPATH, self.TEXT_BASED_BTN.format("Add"))))
        add_btn = self.chrome_driver.find_element(By.XPATH, self.TEXT_BASED_BTN.format("Add"))
        add_btn.click()


    def second_explicitly_wait_example(self):
        # click enable button
        enable_btn = self.chrome_driver.find_element(By.XPATH, self.TEXT_BASED_BTN.format("Enable"))
        log.info("Urmeaza sa dam click pe butonul enable")
        enable_btn.click()
        log.info("Butonul enable a fost apasat")
        # wait until text 'It's enabled!' is shown on the page
        WebDriverWait(self.chrome_driver, 5).until(EC.visibility_of_element_located((By.XPATH, """//p[text()="It's enabled!"]""")))
        # verify if disabled button is visible on the page
        enabled_text = self.chrome_driver.find_element(By.XPATH, """//p[text()="It's enabled!"]""")
        disable_button = self.chrome_driver.find_element(By.XPATH, self.TEXT_BASED_BTN.format(("Disable")))
        if enabled_text.is_displayed():
            if disable_button.is_enabled():
                log.info(f"Butonul {disable_button.text} este activat. Vom da click pe el")
                disable_button.click()
            else:
                log.info(f"Butonul {disable_button.text} nu este activat. Nu putem sa dam click pe el")



    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = ExplicitlyWaitExample()
i1.first_explicitly_wait_example()
i1.second_explicitly_wait_example()
i1.close_session()
