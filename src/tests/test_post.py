import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.pages.LoginPageObject import LoginPageObject
from src.pages.MainPageObject import MainPageObject
from src.pages.NewPostPageObject import NewPostPageObject


class TestPost:
    @pytest.mark.run(order=1)
    def test_post_image(self):
        serv_obj = Service("C://Drivers//chromedriver-win32//chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.blogger.com/about/")
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()

        self.loginpage = LoginPageObject(self.driver)
        self.mainpage = MainPageObject(self.driver)
        self.postpage = NewPostPageObject(self.driver)

        self.loginpage.clickSignIn()
        self.loginpage.setEmail("blogger2.testcase@gmail.com")
        self.loginpage.clickEmailNext()
        self.loginpage.setPassword("bloggertestcaseadmin")
        self.loginpage.clickPasswordNext()

        self.driver.implicitly_wait(time_to_wait=5)
        assert self.mainpage.mainPageCheck()
        self.mainpage.clickNewPostButton()
        assert self.postpage.newPostPageCheck()
        self.postpage.clickInsertImage()
        time.sleep(3)
        self.postpage.clickAddByUrl()
        time.sleep(3)
        self.postpage.setImageUrl("https://static.vecteezy.com/system/resources/previews/005/993/485/original/everything-will-be-ok-quote-quotes-design-lettering-poster-inspirational-and-motivational-quotes-and-sayings-about-life-drawing-for-prints-on-t-shirts-and-bags-stationary-or-poster-vector.jpg")
        time.sleep(3)
        self.postpage.clickSelect()
        time.sleep(3)
        self.postpage.clickPublish()
        time.sleep(3)
        self.postpage.clickConfirm()
        time.sleep(3)
        self.driver.quit()






