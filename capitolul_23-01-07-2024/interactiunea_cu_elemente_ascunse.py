import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from automation.CommonMethods import CommonMethods

class InteractiuneCuElementeAscunse(CommonMethods):
    def __init__(self):
        super().__init__()
        time.sleep(1)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://demoqa.com/")

    def close_session(self):
        self.chrome_driver.quit()



i1 = InteractiuneCuElementeAscunse()
i1.check_visibility("//img[@src='/images/Toolsqa.jpg']")
i1.hide_specific_element("//img[@src='/images/Toolsqa.jpg']")
i1.check_visibility("//img[@src='/images/Toolsqa.jpg']")
i1.close_session()
