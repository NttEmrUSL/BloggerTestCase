import inspect
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def loggerInit(self, name):
   logger = logging.getLogger(name)
   filehandler = logging.FileHandler(filename="testlog", mode='a')
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   filehandler.setFormatter(formatter)
   logger.addHandler(filehandler)
   logger.setLevel(logging.INFO)
   return logger

def setup_method(self, url):
    #webdriver manager , selenium chrome
    serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
    self.driver = webdriver.Chrome(service=serv_obj)
    self.driver.get(url)
    self.driver.implicitly_wait(time_to_wait=10)
    self.driver.maximize_window()
    return self.driver

def error_screenshot(self, method=None):
        if method is None:
            method = inspect.stack()[
                2].function
            file_name = f"C:/Users/10132866/PycharmProjects/pythontraining/BloggerTestCase/src/screenshots_{method}.png"
            self.driver.save_screenshot(file_name)
        else:
            method = inspect.stack()[
                1].function
            file_name = f"C:/Users/10132866/PycharmProjects/pythontraining/BloggerTestCase/src/screenshots_{method}.png"
            self.driver.save_screenshot(file_name)
        print(f"Screenshot '{file_name}' is saved.")






