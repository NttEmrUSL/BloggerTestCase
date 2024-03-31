import time
import pytest


from src.pages import BasePage
from src.pages.Config import Config
from src.pagesObjects.EditPageObject import EditPageObject
from src.pagesObjects.LoginPageObject import LoginPageObject
from src.pagesObjects.PostPageObject import PostPageObject

'''
1 - Open browser and visit https://www.blogger.com/about/
2 - Click sign in button 
3 - Enter email and click next button
4 - Enter password and click next button
5 - Wait until home page loading 
6 - Click the post that has been created
7 - Click the page 
8 - Edit the text with "Hi my Name is Emre"
9 - Click Update button
10 - Click Back button 
'''

class TestCheckEditPost:
    @pytest.mark.run(order=2)
    def test_check_edit_post(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK EDİT POST ----")
        self.logger.info("Open browser and visit https://www.blogger.com/about/")
        self.driver = BasePage.setup_method(self, Config.adminBloggerUrl)

        self.loginpage = LoginPageObject(self.driver)
        self.editpage = EditPageObject(self.driver)
        self.postPage = PostPageObject(self.driver)

        self.logger.info("Click sign in button")
        self.loginpage.clickSignIn()
        self.logger.info("Enter email and click next button")
        self.loginpage.setEmail(Config.adminEmail)
        self.loginpage.clickEmailNext()
        self.logger.info("Enter password and click next button")
        self.loginpage.setPassword(Config.adminPassword)
        self.loginpage.clickPasswordNext()

        self.logger.info("Wait until home page loading")
        self.driver.implicitly_wait(time_to_wait=5)

        self.logger.info("Click the post that has been created")
        self.postPage.clickPostView()
        time.sleep(3)

        self.logger.info("Click the page ")
        self.editpage.clickPage()
        time.sleep(3)

        self.logger.info("Edit the text with 'Hi my Name is Emre' ")
        self.editpage.sendText("Hi my name is Emre")
        time.sleep(3)

        self.logger.info("Click Update button")
        self.editpage.clickUpdateButton()
        time.sleep(3)

        self.logger.info("Click Back button ")
        self.editpage.clickBackToMainPage()
        time.sleep(2)
        self.tearDown()
        self.logger.info("Test Finished Successfully")
    def tearDown(self):
        self.driver.close()
