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
7 - Check comment is deleted
'''

class TestCheckDeleteCommment:
    @pytest.mark.run(order=6)
    def test_check_delete_comment(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK DELETE COMMENT ----")
        self.logger.info("Open browser and visit https://onlinebloggertest.blogspot.com/")
        self.driver = BasePage.setup_method(self, Config.visitorBloggerUrl)

        self.loginpage = LoginPageObject(self.driver)
        self.visitorpage = VisitorPageObject(self.driver)

        try:
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
            self.logger.info("Wait until post page loading")
            time.sleep(3)

            self.logger.info("Check comment is deleted")
            if self.visitorpage.isCommentDeleted():
                assert True
            else:
                assert False
            self.logger.info("Test Finished Successfully")

        except Exception as e:
            self.error_screenshot()
            self.logger.error(f"An error occurred: {str(e)}")

        finally:
            self.tearDown()

    def tearDown(self):
        self.driver.close()
