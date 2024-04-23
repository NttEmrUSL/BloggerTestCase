import time
import pytest


from src.pages import BasePage
from src.pages.Config import Config
from src.pagesObjects.LoginPageObject import LoginPageObject
from src.pagesObjects.PostPageObject import PostPageObject

'''
1 - Open browser and visit https://www.blogger.com/about/
2 - Click sign in button 
3 - Enter email and click next button
4 - Enter password and click next button
5 - Wait until home page loading 
6 - Select Post
7 - Click post delete icon
8 - Click delete confirm button
9 - Wait until home page refresh 
10 - Check post is deleted 
'''

class TestCheckDeletePost:
    @pytest.mark.run(order=7)
    def test_check_delete_post(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK DELETE POST ----")
        self.logger.info("Open browser and visit https://www.blogger.com/about/")
        self.driver = BasePage.setup_method(self, Config.adminBloggerUrl)

        self.loginpage = LoginPageObject(self.driver)
        self.postpage = PostPageObject(self.driver)

        try:
            self.logger.info("Click sign in button")
            self.loginpage.clickSignIn()
            self.logger.info("Enter email and click next button")
            self.loginpage.setEmail(Config.adminEmail)
            self.loginpage.clickEmailNext()
            self.logger.info("Enter password and click next button")
            self.loginpage.setPassword(Config.adminPassword)
            self.loginpage.clickPasswordNext()
            time.sleep(3)

            self.logger.info("Wait until home page loading")
            self.logger.info("Select Post")
            self.logger.info("Click post delete icon")
            self.postpage.clickDeleteIcon()
            time.sleep(3)

            self.logger.info("Click delete confirm button")
            self.postpage.clickDeleteButton()
            time.sleep(3)

            self.logger.info("Wait until home page refresh")
            self.logger.info("Check post is deleted")

            assert self.postpage.isPostDeleted()
            self.logger.info("Test Finished Successfully")

        except Exception as e:
            self.error_screenshot()
            self.logger.error(f"An error occurred: {str(e)}")

        finally:
            self.tearDown()

    def tearDown(self):
        self.driver.close()



