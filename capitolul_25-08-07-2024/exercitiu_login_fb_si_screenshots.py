"""Exercitiu practic Facebook

1) Navigam pe https://www.facebook.com
2) Apasam pe butonul 'Allow all cookies'
3) Completam campul de email cu un email dummy dar care sa respecte formatul unui email obisnuit (@gmail.com, @yahoo.com)
4) Completam parola cu un string dummy
5) Apasam pe butonul de log in
6) Validam ca mesajul 'The email you entered isn’t connected to an account. Create a new Facebook account.' este afisat pe pagina
7) Facem un screenshot care sa cuprinda acest mesaj (folosim metoda save_screenshot)
"""


import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods


class SeleniumScreenshots(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.facebook.com")

    def acc_cookies(self):
        acc_cookies_btn = self.chrome_driver.find_element(By.XPATH, "(//div[@aria-label='Allow all cookies'])[2]")
        acc_cookies_btn.click()
        time.sleep(2)

    def complete_login_details(self, email, password):
        email_field = self.chrome_driver.find_element(By.ID, "email")
        email_field.send_keys(email)
        time.sleep(1)
        password_field = self.chrome_driver.find_element(By.ID, "pass")
        password_field.send_keys(password + Keys.ENTER)
        time.sleep(5)

    def validate_not_connected_email_to_account_msg(self, expected_warning_msg):
        not_connected_ui_text = self.chrome_driver.find_element(By.XPATH, "//div[@id='email_container']//div[@class='_9ay7']").get_attribute("innerText")
        assert not_connected_ui_text == expected_warning_msg, f"Wrong error validation message.Expedcted message was {expected_warning_msg} but the actual message is {not_connected_ui_text}."

    def get_not_connected_email_to_account_msg_screenshot(self):
        self.chrome_driver.find_element(By.XPATH, "//div[@id='email_container']//div[@class='_9ay7']").screenshot("not_connected_email_to_acc_msg.png")

    def close_session(self):
        self.chrome_driver.quit()


expected_warning_msg = "The email you entered isn’t connected to an account. Find your account and log in."
ss_1 = SeleniumScreenshots()
ss_1.acc_cookies()
ss_1.complete_login_details("random129219391@gmail.com", "dsaid9a02dkaskkl")
ss_1.validate_not_connected_email_to_account_msg(expected_warning_msg)
ss_1.get_not_connected_email_to_account_msg_screenshot()
ss_1.close_session()