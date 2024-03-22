import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.LoginPageObject import LoginPageObject
from src.pages.VisitorPageObject import VisitorPageObject

class TestPostComment:
    @pytest.mark.run(order=4)
    def test_post_isvisible(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://onlinebloggertest.blogspot.com/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()
        time.sleep(3)

        self.visitorpage = VisitorPageObject(self.driver)
        self.loginpage = LoginPageObject(self.driver)

        self.visitorpage.clickPostCommentButton()
        time.sleep(5)
        self.visitorpage.clickSignInButton()
        self.loginpage.setEmail("blogger.visitorcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcasevisitor")
        self.loginpage.clickPasswordNext()
        time.sleep(5)

        self.visitorpage.enterComment("What a great post ")
        time.sleep(5)
        self.visitorpage.publishComment()
        time.sleep(5)
        self.driver.quit()


