import pytest


from src.pages import BasePage
from src.pages.Config import Config
from src.pagesObjects.VisitorPageObject import VisitorPageObject

'''
1 - Open browser and visit https://onlinebloggertest.blogspot.com/
2 - Wait until page loading 
3 - Check post visibility
'''

class TestCheckPostIsVisible:
    @pytest.mark.run(order=3)
    def test_check_post_isvisible(self):
        self.logger = BasePage.loggerInit(self, self.__class__.__name__)

        self.logger.info("---- TEST CHECK POST IS VISIBLE ----")
        self.logger.info("Open browser and visit https://onlinebloggertest.blogspot.com/")
        self.driver = BasePage.setup_method(self, Config.visitorBloggerUrl)

        self.visitorpage = VisitorPageObject(self.driver)

        self.logger.info("Check post visibility")
        assert self.visitorpage.isPostVisible()
        self.tearDown()
        self.logger.info("Test Finished Successfully")

    def tearDown(self):
        self.driver.close()