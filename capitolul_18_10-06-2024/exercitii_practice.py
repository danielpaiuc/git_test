"""
1. Sa se acceseze urmatoarea adresa web: https://olx.ro
2. Sa se maximize fereastra de lucru
3. Sa se deschida un alt tab in care sa se navigheze catre https://facebook.com
4. Sa se inchida tab-ul cu site-ul olx
5. Sa se deschida un alt tab cu adresa https://demoqa.com
6. Sa se dea refresh la pagina cu demoaqa.com
7. Sa se inchida sesiunea de ChromeDriver
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options_object = Options()
chrome_options_object.add_experimental_option("detach", True)

service_object = Service(executable_path= r"C:\Users\paiuc\PycharmProjects\QA_automation_python_entry_level\automation\chromedriver.exe")

# 1) Pornim sesiunea de ChromeDriver
chrome_driver = webdriver.Chrome(service=service_object, options=chrome_options_object)

# 1.1) Accesare olx

chrome_driver.get("https://olx.ro")

# 2) Maximizare fereastra
chrome_driver.maximize_window()
# 3) Deschidere new tab facebook

chrome_driver.execute_script("window.open('https://facebook.com', '_blank');")

# 4. Sa se inchida tab-ul cu site-ul olx
chrome_driver.close()

# 5. deschide alt tab demoqa
chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
chrome_driver.execute_script("window.open('https://demoqa.com', '_blank');")
# 6. sa se dea refresh la demoqa
chrome_driver.switch_to.window(chrome_driver.window_handles[1])
chrome_driver.refresh() # linia 42 am mutat focusul pe demoqa si pe linia 43 am facut refresh pe pagina dorita(demoqa)
#7
time.sleep(2)
chrome_driver.quit()
