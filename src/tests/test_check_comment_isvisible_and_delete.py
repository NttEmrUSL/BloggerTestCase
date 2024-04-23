import time
import pytest

from src.pages import BasePage
from src.pages.Config import Config
from src.pagesObjects.CommentPageObject import CommentPageObject
from src.pagesObjects.LoginPageObject import LoginPageObject
from src.pagesObjects.MainPageObject import MainPageObject
from src.pagesObjects.VisitorPageObject import VisitorPageObject


'''
1 - Open browser and visit https://www.blogger.com/about/
2 - Click sign in button 
3 - Enter email and click next button
4 - Enter password and click next button
5 - Wait until home page loading 
6 - Click Comment Button
7 - Check comment is visible
8 - Click delete icon 
9 - Click delete confirm button
'''

class TestCheckCommentIsVisibleAndDelete:
    @pytest.mark.run(order=5)
    def test_check_comment_isvisible_and_delete(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK COMMENT IS VISIBLE AND DELETE ----")
        self.logger.info("Open browser and visit https://www.blogger.com/about/")
        self.driver = BasePage.setup_method(self, Config.adminBloggerUrl)

        self.loginpage = LoginPageObject(self.driver)
        self.mainpage = MainPageObject(self.driver)
        self.commentpage = CommentPageObject(self.driver)
        self.visitorpage = VisitorPageObject(self.driver)

        try:
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

            self.logger.info("Click Comment Button")
            self.mainpage.clickCommentButton()
            time.sleep(3)

            self.logger.info("Check comment is visible")
            self.commentpage.checkCommentText(self.visitorpage.comment_text)
            time.sleep(3)

            self.logger.info("Click delete icon ")
            self.commentpage.clickDeleteIcon()
            time.sleep(3)

            self.logger.info("Click delete confirm button")
            self.commentpage.clickDeleteButton()
            time.sleep(3)

            self.logger.info("Test Finished Successfully")

        except Exception as e:
            self.error_screenshot()
            self.logger.error(f"An error occurred: {str(e)}")

        finally:
            self.tearDown()

    def tearDown(self):
        self.driver.close()


