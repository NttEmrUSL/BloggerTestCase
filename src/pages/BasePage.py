import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def loggerInit(self, name):
   logger = logging.getLogger(name)
   filehandler = logging.FileHandler(filename="testlog", mode='w')
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   filehandler.setFormatter(formatter)
   logger.addHandler(filehandler)
   logger.setLevel(logging.INFO)
   return logger

def setup_method(self, url):
    serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
    self.driver = webdriver.Chrome(service=serv_obj)
    self.driver.get(url)
    self.driver.implicitly_wait(time_to_wait=10)
    self.driver.maximize_window()
    return self.driver






