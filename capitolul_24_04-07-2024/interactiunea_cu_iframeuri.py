import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods


class SchimbareIFrame(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://testpages.herokuapp.com/styled/iframes-test.html")

    def click_nested_page_index_link(self):
        index_btn = self.chrome_driver.find_element(By.XPATH, "//h1[text()='Nested Page Example']//..//a")
        index_btn.click()
        time.sleep(2)

    def switch_to_iframe_by_webelement(self, iframe_locator_xpath):
        # Schimbarea iframe-ului folosind un locator unic pentru iframe-ul catre care vrem sa facem switch-ul
        self.chrome_driver.switch_to.frame(self.chrome_driver.find_element(By.XPATH, iframe_locator_xpath))

    def switch_to_iframe_by_index(self, iframe_index):
        self.chrome_driver.switch_to.frame(iframe_index)

    def close_session(self):
        self.chrome_driver.quit()


i1 = SchimbareIFrame()
i1.switch_to_iframe_by_webelement("//iframe[@id='thedynamichtml']")
i1.scroll_x_y_axis_by_value(y_axis_scroll_value=100)
time.sleep(1)
i1.scroll_x_y_axis_by_value(y_axis_scroll_value=100)
time.sleep(1)
i1.scroll_x_y_axis_by_value(y_axis_scroll_value=100)
i1.chrome_driver.switch_to.default_content()
# i1.switch_to_iframe_by_webelement("//iframe[@id='theheaderhtml']")
i1.switch_to_iframe_by_index(1)
i1.click_nested_page_index_link()
i1.close_session()