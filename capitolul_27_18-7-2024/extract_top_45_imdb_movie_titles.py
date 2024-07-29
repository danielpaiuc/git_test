import time
from selenium.webdriver.common.by import By
from automation.CommonMethods import CommonMethods
from selenium.webdriver.common.action_chains import ActionChains

class ExtractMovieTitles(CommonMethods):

    def __init__(self):
        super().__init__()
        time.sleep(2)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(url="https://www.imdb.com/")
        self.chrome_driver.implicitly_wait(5)

    def change_frame_by_index(self, frame_index):
        self.chrome_driver.switch_to.frame(frame_index)


    def accept_cookies(self):
        ac = self.chrome_driver.find_element(By.XPATH, "//button[@data-testid='accept-button']")
        ac.click()

    def menu_selection(self):
        ms = self.chrome_driver.find_element(By.XPATH, "//span[@class='ipc-responsive-button__text']")
        ms.click()

    def top_movies(self):
        time.sleep(1)
        tm = self.chrome_driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']")
        tm.click()

    def reject_site_preferences(self):
        rsp = self.chrome_driver.find_element(By.XPATH, "//button[@data-testid='reject-button']")
        rsp.click()

    def extract_top45(self):
        time.sleep(2)
        movie_list = self.chrome_driver.find_elements(By.XPATH, "//ul//h3[@class='ipc-title__text']")
        top45_movies = []
        print(len(movie_list))
        for movie in movie_list[0:45]:
            top45_movies.append(movie.text)

        file_1 = open(r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\top_45_imdb_movies.txt", mode="w")
        for film in top45_movies:
            file_1.write(film + "\n")


    def close_session(self):
        time.sleep(2)
        self.chrome_driver.quit()


i1 = ExtractMovieTitles()
i1.accept_cookies()
i1.menu_selection()
i1.top_movies()
#i1.reject_site_preferences()
i1.extract_top45()
i1.close_session()