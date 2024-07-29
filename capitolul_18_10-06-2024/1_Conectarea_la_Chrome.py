import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Ne cream o noua instanta de Chrome folosind componenta de ChromeDriver

#Varianta 1 - fara sa descarcam ChromeDriver si sa ii dam calea catre ChromeDriver
# chrome_driver = webdriver.Chrome()

"""
Limitari pentru varianta 1:

1) Se poate ca versiunea noastra de chrome sa fie foarte veche si atunci cand incearca sa descarce automat versiunea
de ChromeDriver specifica pentru versiunea noastra foarte veche de Chrome, sa nu o gaseasca.

2) Se poate ca versiunea noastra de Chrome sa fie foarta noua si atunci cand incearca sa descarce versiunea specifica
de ChromeDriver sa nu o gasesaca pe site-ul de unde descarca.

3) Cel mai bine e sa merge pe ultima varianta de Chrome
"""

"""
!!! Pentru ca sesiunea de ChromeDriver sa nu se mai inchida automat dupa ce se executa pasii din test, ne cream o
instanta de tip Options(o instanta a clasei Options) si apelam metoda add_experimental_option cu parametrii ("detach", True)

Instanta noastra trebuie sa fie data in instanta noastra de ChromeDriver, pentru parametrul options.

Daca vreau ca instanta de ChromeDriver sa se inchida automat la final, las al doilea parametru ca fiind False
"""

# Varianta 2 - ii dam calea catre ChromeDriver

chrome_options_obj = Options()
chrome_options_obj.add_experimental_option("detach", True)

service_obj = Service(executable_path=r"E:\QA_Automation_Python_Entry_Level\Automation\chromedriver.exe")

# 1) Pornim sesiunea de ChromeDriver
chrome_driver = webdriver.Chrome(service=service_obj, options=chrome_options_obj)

time.sleep(2)

# 2) Maximizam fereastra de lucru (Metoda maximize_window -> maximizeaza fereastra de lucru)

chrome_driver.maximize_window()

# 3) Navigam catre un anumit URL(URL-ul trebuie sa contina https sau http, altfel nu va functiona)

chrome_driver.get("https://google.com")

# 4) Navigam catre o alta adresa web dar dintr-un alt tab

# 4.1) Deschidem cel de al doilea tab blank

chrome_driver.execute_script("window.open('', '_blank');")

chrome_driver.execute_script("window.open('https://python.org', '_blank');"
                             "window.open('https://altex.ro', '_blank');")


chrome_driver.get("https://demoqa.com") # => ne va deschide adresa tot in primul tab deoarece nu si-a schimbat
# focusul de pe tab-ul curent

# 4.2) Pentru a schimba focusul de pe tab-ul 1(cel cu adresa google.com) pe cel de al doilea tab(cel blank deschis mai devrmee)
# ne folosim de chrome_driver.switch_to.window(chrome_driver.window_handles[1])

chrome_driver.switch_to.window(chrome_driver.window_handles[1])
chrome_driver.get("https://altex.ro")
time.sleep(2)

"""
La finalul executiei unui test automat, vrem ca instanta de ChromeDriver sa se inchida.De aceea, fie nu ne mai folosim
de parametrul options din variabila chrome_drive, fie inchidem testul respectiv folosind metoda de quit() sau close().
"""

chrome_driver.close() # => va inchide doar tab-ul curent(tab-ul pe care este focusul in momentul respectiv

chrome_driver.quit() # => va inchide toata fereastra(sesiunea curenta de ChromeDriver)



