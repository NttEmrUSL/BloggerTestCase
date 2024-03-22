import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.EditPageObject import EditPageObject
from src.pages.LoginPageObject import LoginPageObject
from src.pages.PostPageObject import PostPageObject


class TestEditPost:
    @pytest.mark.run(order=2)
    def test_edit_post(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.blogger.com/about/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()

        self.loginpage = LoginPageObject(self.driver)
        self.editpage = EditPageObject(self.driver)
        self.postPage = PostPageObject(self.driver)

        self.loginpage.clickSignIn()
        self.loginpage.setEmail("blogger2.testcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcaseadmin")
        self.loginpage.clickPasswordNext()

        self.driver.implicitly_wait(time_to_wait=5)
        self.postPage.clickPostView()
        time.sleep(3)
        self.editpage.clickPage()
        time.sleep(3)
        self.editpage.sendText("Hi my name is Emre")
        time.sleep(3)
        self.editpage.clickUpdateButton()
        time.sleep(3)
        self.editpage.clickBackToMainPage()
        time.sleep(2)
        self.driver.quit()

