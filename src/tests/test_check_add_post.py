import pytest
import time

from src.pages import BasePage
from src.pagesObjects.LoginPageObject import LoginPageObject
from src.pagesObjects.MainPageObject import MainPageObject
from src.pagesObjects.NewPostPageObject import NewPostPageObject
from src.pages.Config import Config


'''
1 - Open browser and visit https://www.blogger.com/about/
2 - Click sign in button 
3 - Enter email and click next button
4 - Enter password and click next button
5 - Wait until home page loading 
6 - Click New Post Button
7 - Click Insert Image icon
8 - Click By Url button
9 - Enter image url 
10 - Click select button
11 - Click publish button
12 - Click confirm button 
'''


class TestCheckAddPost():
    @pytest.mark.run(order=1)
    def test_check_add_post(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK ADD POST ----")
        self.logger.info("Open browser and visit https://www.blogger.com/about/")
        self.driver = BasePage.setup_method(self, Config.adminBloggerUrl)

        self.loginpage = LoginPageObject(self.driver)
        self.mainpage = MainPageObject(self.driver)
        self.postpage = NewPostPageObject(self.driver)

        self.logger.info("Click sign in button")
        self.loginpage.clickSignIn()
        self.logger.info("Enter email and click next button")
        self.loginpage.setEmail(Config.adminEmail)
        self.loginpage.clickEmailNext()

        self.logger.info("Enter password and click next button")
        self.loginpage.setPassword(Config.adminPassword)
        self.loginpage.clickPasswordNext()

        self.logger.info("Wait until home page loading ")
        self.driver.implicitly_wait(time_to_wait=5)
        assert self.mainpage.mainPageCheck()

        self.logger.info("Click New Post Button")
        self.mainpage.clickNewPostButton()

        assert self.postpage.newPostPageCheck()

        self.logger.info("Click Insert Image icon")
        self.postpage.clickInsertImage()
        time.sleep(3)

        self.logger.info("Click By Url button")
        self.postpage.clickAddByUrl()
        time.sleep(3)

        self.logger.info("Enter image url")
        self.postpage.setImageUrl(Config.imageurl)
        time.sleep(3)

        self.logger.info("Click select button")
        self.postpage.clickSelect()
        time.sleep(3)

        self.logger.info("Click publish button")
        self.postpage.clickPublish()
        time.sleep(3)

        self.logger.info("Click confirm button")
        self.postpage.clickConfirm()

        time.sleep(3)
        self.tearDown()
        self.logger.info("Test Finished Successfully")

    def tearDown(self):
        self.driver.close()




