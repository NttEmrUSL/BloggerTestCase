import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.LoginPageObject import LoginPageObject
from src.pages.MainPageObject import MainPageObject
from src.pages.PostPageObject import PostPageObject


class TestPostDelete:
    @pytest.mark.run(order=7)
    def testPostDelete(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.blogger.com/about/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()
        time.sleep(3)

        self.loginpage = LoginPageObject(self.driver)
        self.postpage = PostPageObject(self.driver)

        self.loginpage.clickSignIn()
        self.loginpage.setEmail("blogger2.testcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcaseadmin")
        self.loginpage.clickPasswordNext()
        time.sleep(3)

        self.postpage.clickDeleteIcon()
        time.sleep(3)
        self.postpage.clickDeleteButton()
        time.sleep(3)
        assert self.postpage.isPostDeleted()
        self.driver.quit()




