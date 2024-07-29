import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods


class ImplicitlyWaitExample(CommonMethods):

    def __init__(self):
        super().__init__()
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://facebook.com")
        self.chrome_driver.implicitly_wait(5)


    def acc_cookies(self):
        acc_cookies_btn = self.chrome_driver.find_element(By.XPATH, "(//div[@aria-label='Allow all cookies'])[2]")
        acc_cookies_btn.click()



    def create_new_account(self):
        create_new_account_bttn = self.chrome_driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
        create_new_account_bttn.click()
        first_name_field = self.chrome_driver.find_element(By.XPATH, "//input[@name='firstname']")
        first_name_field.send_keys("First name 123")


    def close_session(self):
        #time.sleep(2)
        self.chrome_driver.quit()


i1 = ImplicitlyWaitExample()
i1.acc_cookies()
i1.create_new_account()
i1.close_session()