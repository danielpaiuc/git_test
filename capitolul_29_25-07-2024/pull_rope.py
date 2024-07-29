"""
Pull rope exercise
"""

import time
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains
from automation.capitolul_28_22_07_2024.implementare_logger import logger as log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PullRope(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://jenniferdewalt.com/node/hello_world")
        self.chrome_driver.implicitly_wait(5)


    def close_session(self):
        time.sleep(5)
        self.chrome_driver.quit()

    def pull_rope(self):
        pull_rope_button = self.chrome_driver.find_element(By.XPATH, "//img[@id='rope']")
        actions = ActionChains(self.chrome_driver)
        actions.drag_and_drop_by_offset(pull_rope_button, 0, 200).perform()


i1 = PullRope()
i1.pull_rope()
i1.close_session()

