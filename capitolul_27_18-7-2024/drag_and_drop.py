import time

from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains

class DragAndDrop(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://jqueryui.com/droppable/")
        self.chrome_driver.implicitly_wait(5)

    def drag_and_drop_test(self):
        # 0) Schimbam i-framul
        # 1) Identificam elementul sursa (elementul pe care vrem sa il tragem)
        # 2) Identificam elementul destinatie (elementul unde vrem sa facem drop-ul)
        # 3) Executam actiunea de drag and drop de la elementul sursa la elementul destinatie
        self.chrome_driver.switch_to.frame(0)
        source = self.chrome_driver.find_element(By.ID, "draggable")
        target = self.chrome_driver.find_element(By.CSS_SELECTOR, "#droppable")
        actions = ActionChains(self.chrome_driver)
        actions.drag_and_drop(source, target).perform()


    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = DragAndDrop()
i1.drag_and_drop_test()
i1.close_session()