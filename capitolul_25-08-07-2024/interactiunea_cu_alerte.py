import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods


class InteractiuneCuAlerte(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://demoqa.com/alerts")

    def click_first_alert_btn(self):
        first_alert_btn = self.chrome_driver.find_element(By.ID, "alertButton")
        first_alert_btn.click()
        time.sleep(1)
        switch_alert = self.chrome_driver.switch_to.alert
        print(type(switch_alert))
        switch_alert.accept()
        time.sleep(1)

    def click_second_alert_btn(self):
        second_alert_btn = self.chrome_driver.find_element(By.CSS_SELECTOR, "#timerAlertButton")
        second_alert_btn.click()
        time.sleep(5.5)
        switch_alert = self.chrome_driver.switch_to.alert
        switch_alert.accept()
        time.sleep(1)

    def click_third_alert_btn(self):
        third_alert_btn = self.chrome_driver.find_element(By.XPATH, "//button[@id='confirmButton']")
        third_alert_btn.click()
        time.sleep(1)
        switch_alert = self.chrome_driver.switch_to.alert
        print("Verificam ca textul din alerta este cel cautat")
        assert switch_alert.text == "Do you confirm action?", "Textul alertei nu este potrivit"
        print("Apasam butonul 'Cancel' din alerta deschisa")
        switch_alert.dismiss()
        cancel_confirmation_text = self.chrome_driver.find_element(By.XPATH,
                                                                   "//span[@id='confirmResult']").get_attribute(
            "innerHTML")
        print("Verificam textul aparut pe ecran dupa ce s-a anulat alerta")
        expected_text_after_cancel = "You selected Cancel"
        assert cancel_confirmation_text == expected_text_after_cancel, f"Textul afisat in urma anularii alertei nu este cel corect.S-a afisat textul {cancel_confirmation_text} in loc {expected_text_after_cancel}"
        third_alert_btn.click()
        time.sleep(1)
        switch_alert = self.chrome_driver.switch_to.alert
        switch_alert.accept()
        time.sleep(1)
        ok_confirmation_text = self.chrome_driver.find_element(By.XPATH, "//span[@id='confirmResult']").get_attribute(
            "innerHTML")
        expected_text_after_ok = "You selected Ok"
        assert ok_confirmation_text == expected_text_after_ok, f"Textul afisat in urma confirmarii alertei nu este cel corect.S-a afisat textul {ok_confirmation_text} in loc {expected_text_after_ok}"
        time.sleep(1)

    def click_fourth_alert_btn(self, alert_input_text):
        fourth_alert_btn = self.chrome_driver.find_element(By.CSS_SELECTOR, "button[id=promtButton]")
        fourth_alert_btn.click()
        time.sleep(2)
        """
        Exercitiu practic:

        1) Validam ca textul alertei este 'Please enter your name' folosind assert
        2) Introducem un string oarecare(text_string) in campul de sub labelul 'Please enter your name'
        3) Apasam Ok pentru a inchide alerta
        4) Validam ca textul 'You entered text_string' este afisat pe ecran
        """
        # 1) Validam ca textul alertei este 'Please enter your name' folosind assert
        switch_alert = self.chrome_driver.switch_to.alert
        expected_alert_label_text = 'Please enter your name'
        assert switch_alert.text == expected_alert_label_text, f"Invalid text -> expected text was '{expected_alert_label_text}' but '{switch_alert.text}' is shown"

        # 2) Introducem un string oarecare(text_string) in campul de sub labelul 'Please enter your name'
        switch_alert.send_keys(alert_input_text)

        # 3) Apasam Ok pentru a inchide alerta
        switch_alert.accept()

        # 4) Validam ca textul 'You entered text_string' este afisat pe ecran
        ok_confirmation_text = self.chrome_driver.find_element(By.XPATH, "//span[@id='promptResult']").get_attribute(
            "innerHTML")
        expected_text_after_ok = f"You entered {alert_input_text}"
        assert ok_confirmation_text == expected_text_after_ok, f"Textul afisat in urma confirmarii alertei nu este cel corect.S-a afisat textul {ok_confirmation_text} in loc {expected_text_after_ok}"
        time.sleep(2)

    def close_session(self):
        self.chrome_driver.quit()


i1 = InteractiuneCuAlerte()
i1.click_first_alert_btn()
i1.click_second_alert_btn()
i1.click_third_alert_btn()
i1.click_fourth_alert_btn("text to be sent in the alert")
i1.close_session()