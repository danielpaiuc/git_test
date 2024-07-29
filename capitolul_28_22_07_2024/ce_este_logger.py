import logging

"""
Link documentatie oficiala: https://docs.python.org/3/library/logging.html

Logger-ul are 6 levels:

1) NOTSET (0)
2) DEBUG (10)
3) INFO (20)
4) WARNING (30)
5) ERROR (40)
6) CRITICAL (50)

Doar mesajele cu severitate cel putin egale cu warning sunt afisate in consola, by default (loggerul e setat pe warning).
"""

logging.basicConfig(level=20, format='%(asctime)s - %(levelname)s - %(message)s', filename="curs_selenium_python.log", filemode='w')

logging.debug("Acesta este un mesaj de debug")
logging.info("Acesta este un mesaj de informare")
logging.warning("Acesta este un mesaj de atentionare")
logging.error("Acesta este un mesaj de eroare")
logging.critical("Mesaj CRITICAL")