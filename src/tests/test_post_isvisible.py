import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.VisitorPageObject import VisitorPageObject


class TestPostIsVisible:
    @pytest.mark.run(order=3)
    def test_post_isvisible(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://onlinebloggertest.blogspot.com/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()
        time.sleep(3)
        self.visitorpage = VisitorPageObject(self.driver)

        if self.visitorpage.isPostVisible():
            assert True
        else:
            assert False

        self.driver.quit()