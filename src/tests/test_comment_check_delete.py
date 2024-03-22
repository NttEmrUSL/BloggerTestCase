import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.CommentPageObject import CommentPageObject
from src.pages.LoginPageObject import LoginPageObject
from src.pages.MainPageObject import MainPageObject
from src.pages.VisitorPageObject import VisitorPageObject


class TestCommentCheckDelete:
    @pytest.mark.run(order=5)
    def test_comment_check_delete(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.blogger.com/about/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()
        time.sleep(3)

        self.loginpage = LoginPageObject(self.driver)
        self.mainpage = MainPageObject(self.driver)
        self.commentpage = CommentPageObject(self.driver)
        self.visitorpage = VisitorPageObject(self.driver)

        self.loginpage.clickSignIn()
        self.loginpage.setEmail("blogger2.testcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcaseadmin")
        self.loginpage.clickPasswordNext()

        self.mainpage.clickCommentButton()
        time.sleep(3)

        self.commentpage.checkCommentText(self.visitorpage.comment_text)
        time.sleep(3)
        self.commentpage.clickDeleteIcon()
        time.sleep(3)
        self.commentpage.clickDeleteButton()
        time.sleep(3)
        self.driver.quit()




