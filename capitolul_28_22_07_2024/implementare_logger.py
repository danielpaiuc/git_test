import logging

class MyLogger:

    def __init__(self):
        self.logger = logging.getLogger(MyLogger.__name__) # returneaza numele logger-ului
        self.logger.setLevel(logging.INFO)

        # Dupa ce obiectul a fost creat, el va fi trimis mai departe catre un handler

        self.console_handler = logging.StreamHandler()

        # Ne asiguram ca avem un handler pentru consola

        self.console_handler.setLevel(logging.INFO)

        # Ne stabilim un format pentru loguri

        logger_format = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')

        # Setam logger_format ul creat pentru a functiona cu handler-ul consolei

        self.console_handler.setFormatter(logger_format)

        #Adaugam handler ul catre conola la loggerul nostru

        self.logger.addHandler(self.console_handler)

logger = MyLogger().logger

logger.info("Mesaj de informare")
logger.debug("Mesaj de DEBUG")