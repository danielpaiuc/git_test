"""
Test Login cu credentiale valide
1. Navigam pe https://www.w3schools.com/html/html_iframe.asp
2. Apasam pe butonul de accept cookies
3. Schimbam iframe-ul catre cel care are titlul 'W3Schools HTML Tutorial'
4. Apasam pe butonul de accept cookies din iframe-ul catre catre am navigat la pasul 3
5. Apasam pe butonul 'Forgot Password?'
6. Completam campul de email cu un email cu o forma valida( sa contina @ceva.com)
7. Apasam pe butonul 'Reset password'
8. Validam ca mesajul 'We've sent an email to <adresa_email> with instructions a aparut pe pagina.

Test Login cu email cu format incorect
1. Navigam pe https://www.w3schools.com/html/html_iframe.asp
2. Schimbam iframe-ul catre cel care are titlul 'W3Schools HTML Tutorial'
3. Apasam pe Log In in noul iframe
4. Completam campul de email cu un email cu o forma invalida(fara @)
5. Completam parola
6. Validam ca mesajul 'Looks like you forgot something' e vizibil pe pagina
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
adresa_email = "nume.prenume@vodafone.com"
class SchimbareIFrame(CommonMethods):
    def __init__(self):
        super().__init__()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.w3schools.com/html/html_iframe.asp")

    def accept_cookies_1(self):
        a = self.chrome_driver.find_element(By.XPATH, "//div[@id='accept-choices']")
        a.click()

    def close_session(self):
        self.chrome_driver.quit()

    def switch_to_iframe_by_webelement(self, iframe_locator_xpath):
        self.chrome_driver.switch_to.frame(self.chrome_driver.find_element(By.XPATH, iframe_locator_xpath))

    def click_login(self):
        a = self.chrome_driver.find_element(By.XPATH, "//a[@class = 'user-anonymous tnb-login-btn w3-bar-item w3-btn bar-item-hover w3-right ws-light-green ga-top ga-top-login']")
        a.click()

    def click_forgot_password(self):
        b = self.chrome_driver.find_element(By.XPATH, '//button[@class="CustomButton_button__V5-G+ LoginForm_login_reset_password_button__b1gqW CustomButton_secondary__DiXZj"]')
        b.click()

    def fill_in_email(self, email_address):
        email = self.chrome_driver.find_element(By.XPATH, "//input[contains(@class, 'ResetPasswordForm_reset_password_email')]")
        email.send_keys(email_address)
        time.sleep(2)

    def reset_password(self):
        password_reset = self.chrome_driver.find_element(By.XPATH, '//button[text()="Reset Password"]')
        password_reset.click()

    def check_verification_message(self, string):
        message = self.chrome_driver.find_element(By.XPATH, f'//div[text()="We’ve sent an email to {adresa_email} with instructions."]').text
        if message == string:
            print("Mesajul a fost validat")
        else:
            print("Mesajul nu a fost validat")



s1 = SchimbareIFrame()
s1.accept_cookies_1()
time.sleep(2)
s1.switch_to_iframe_by_webelement("//iframe[@title='W3Schools HTML Tutorial']")
time.sleep(2)
s1.accept_cookies_1()
time.sleep(2)
s1.click_login()
time.sleep(3)
s1.scroll_x_y_axis_by_value(0, 200)
s1.click_forgot_password()
time.sleep(3)
s1.fill_in_email(email_address=adresa_email)
time.sleep(3)
s1.reset_password()
time.sleep(3)
s1.check_verification_message(f"We’ve sent an email to {adresa_email} with instructions.")
s1.close_session()

