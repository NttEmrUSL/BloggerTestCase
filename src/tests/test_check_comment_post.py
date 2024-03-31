import time
import pytest

from src.pages import BasePage
from src.pages.Config import Config
from src.pagesObjects.LoginPageObject import LoginPageObject
from src.pagesObjects.VisitorPageObject import VisitorPageObject

'''
1 - Open browser and visit https://onlinebloggertest.blogspot.com/
2 - Click "Post a Comment" button
3 - Click "Sign in With Google" button
4 - Enter email and click next button
5 - Enter password and click next button
6 - Wait until post page loading 
7 - Click Enter Comment textbox
8 - Enter a comment
9 - Click Publish button
'''


class TestCheckCommentPost:
    @pytest.mark.run(order=4)
    def test_check_comment_post(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK COMMENT POST ----")
        self.logger.info("Open browser and visit https://onlinebloggertest.blogspot.com/")
        self.driver = BasePage.setup_method(self, Config.visitorBloggerUrl)

        self.visitorpage = VisitorPageObject(self.driver)
        self.loginpage = LoginPageObject(self.driver)

        self.logger.info("Click 'Post a Comment' button")
        assert self.visitorpage.visitorPageCheck()
        self.visitorpage.clickPostCommentButton()
        time.sleep(3)

        self.logger.info("Click 'Sign in With Google' button")
        self.visitorpage.clickSignInButton()

        self.logger.info("Enter email and click next button")
        self.loginpage.setEmail(Config.visitorEmail)
        self.loginpage.clickEmailNext()

        self.logger.info("Enter password and click next button")
        self.loginpage.setPassword(Config.visitorPassword)
        self.loginpage.clickPasswordNext()
        time.sleep(3)

        self.logger.info("Wait until post page loading ")
        self.logger.info("Click Enter Comment textbox")
        self.logger.info("Enter a comment")

        self.visitorpage.enterComment("What a great post ")
        time.sleep(3)

        self.logger.info("Click Publish button")
        self.visitorpage.publishComment()
        time.sleep(3)
        self.tearDown()
        self.logger.info("Test Finished Successfully")
    def tearDown(self):
        self.driver.close()