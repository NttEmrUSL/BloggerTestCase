import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class CommentPageObject:

    commentText_css = "div[class='Opvl3b']"
    commentItem_xpath = "(//div[@class='opmHNc'])[1]"
    commentDeleteIcon_xpath = "//*[@id='yDmH0d']/c-wiz[2]/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div/span/div/div/div[4]/div[3]/span/span/span"
    commentDeleteButton_xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"

    def __init__(self,driver):
        self.driver = driver

    #Check comment is true
    #params string commentvisitor: Comment which visitor wrote
    def checkCommentText(self, commentvisitor):
        comment = self.driver.find_element(By.CSS_SELECTOR, self.commentText_css)

        print(comment.text)
        print(commentvisitor)

        if comment.text == commentvisitor:
            assert True
        else:
            assert False

    #Click delete icon
    def clickDeleteIcon(self):
        action = ActionChains(self.driver)
        itemlist = self.driver.find_element(By.XPATH, self.commentItem_xpath)
        action.move_to_element(itemlist).perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.commentDeleteIcon_xpath).click()

    #Click delete button
    def clickDeleteButton(self):
        self.driver.find_element(By.XPATH, self.commentDeleteButton_xpath).click()






