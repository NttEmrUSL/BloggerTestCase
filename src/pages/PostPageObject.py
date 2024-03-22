import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class PostPageObject:

    viewPost_css = "a[href='./blog/post/edit/2581916393429811882/7547949017194907599']"
    postItem_xpath = "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div"
    postItemDeleteIcon_xpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    postItemDeleteButton_xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Trash post'])[2]"
    post_count_class = "yGrhUb"

    def __init__(self, driver):
        self.driver = driver

    def clickPostView(self):
        self.driver.find_element(By.CSS_SELECTOR, self.viewPost_css).click()

    def clickDeleteIcon(self):
        action = ActionChains(self.driver)
        itemlist = self.driver.find_element(By.XPATH, self.postItem_xpath)
        action.move_to_element(itemlist).perform()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.postItemDeleteIcon_xpath).click()

    def clickDeleteButton(self):
        self.driver.find_element(By.XPATH, self.postItemDeleteButton_xpath).click()


    def isPostDeleted(self):
        posts = self.driver.find_elements(By.CLASS_NAME, self.post_count_class)
        if len(posts) <= 1:
            return True
        else:
            return False
