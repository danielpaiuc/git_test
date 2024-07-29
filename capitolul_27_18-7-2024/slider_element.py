import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains

class SliderAction(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://jqueryui.com/slider/")
        self.chrome_driver.implicitly_wait(5)

    def change_frame_by_index(self, frame_index):
        self.chrome_driver.switch_to.frame(frame_index)


    def sliding_method_by_pixels(self):
        # 0) Schimbam i-framul
        # 1) Identificam elementul pe care vrem sa facem slide
        # 2) Executam actiunea de drag and drop folosind un offset bazat pe pixeli
        # 3) Executam actiunea de drag and drop de la elementul sursa la elementul destinatie
        #self.chrome_driver.switch_to.frame(0)
        slider_button = self.chrome_driver.find_element(By.XPATH, "//div[@id='slider']/span")

        actions = ActionChains(self.chrome_driver)
        actions.drag_and_drop_by_offset(slider_button, 583, 0).perform()

    def slide_element_by_percentage(self, slider_element_xpath, percentage):
        #self.chrome_driver.switch_to.frame(0)
        # 2) Identificam elementul care face slide (casuta sau cerculetul de slide)
        slider_button = self.chrome_driver.find_element(By.XPATH, slider_element_xpath)

        # 3) Modificam atributul style pentru slider button in functie de procentul pana la care vrem sa faca slide
        print(slider_button.get_attribute("style"))
        print(f"Ducem elementul de tip slider pana la prcocentul de {percentage}")
        self.chrome_driver.execute_script(f"arguments[0].setAttribute('style', 'left: {percentage}%;')", slider_button)


    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = SliderAction()
i1.change_frame_by_index(0)
#i1.sliding_method_by_pixels()
i1.slide_element_by_percentage("//div[@id='slider']/span", "66")
i1.close_session()