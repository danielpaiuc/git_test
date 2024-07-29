import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains

class WindowSize(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://demoqa.com/")
        self.chrome_driver.implicitly_wait(5)

    def change_frame_by_index(self, frame_index):
        self.chrome_driver.switch_to.frame(frame_index)


    def get_window_size_using_execute_script(self):
        window_height = self.chrome_driver.execute_script("return window.innerHeight;")
        window_width = self.chrome_driver.execute_script("return window.innerWidth;")
        print(f"Current window size is Width = {window_width} x Height = {window_height}")


    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = WindowSize()
i1.get_window_size_using_execute_script()
print(i1.chrome_driver.get_window_size())
i1.chrome_driver.set_window_size(500, 670)
print(i1.chrome_driver.get_window_size())
i1.close_session()