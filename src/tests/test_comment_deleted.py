import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.LoginPageObject import LoginPageObject
from src.pages.VisitorPageObject import VisitorPageObject


class TestCommentDeleted:
    @pytest.mark.run(order=6)
    def test_comment_deleted(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://onlinebloggertest.blogspot.com/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()
        time.sleep(3)

        self.loginpage = LoginPageObject(self.driver)
        self.visitorpage = VisitorPageObject(self.driver)

        assert self.visitorpage.visitorPageCheck()
        self.visitorpage.clickPostCommentButton()
        time.sleep(3)
        self.visitorpage.clickSignInButton()
        self.loginpage.setEmail("blogger.visitorcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcasevisitor")
        self.loginpage.clickPasswordNext()
        time.sleep(3)

        if self.visitorpage.isCommentDeleted():
            assert True
        else:
            assert False

        self.driver.quit()