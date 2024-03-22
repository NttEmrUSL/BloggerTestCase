from selenium.webdriver.common.by import By

class VisitorPageObject:

    postFeatured_id = "FeaturedPost1"
    buttonPostComment_css = "span[class='num_comments']"
    buttonSignWithGoogle_css = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div[1]"
    textareaComment_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea"
    buttonPublish_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div"
    viewComments_xpath = "//li[@class='comment']"

    comment_id = "c8119086250835364148"
    comment_text = "What a great post"

    def __init__(self, driver):
        self.driver = driver

    def isPostVisible(self):
        post = self.driver.find_elements(By.ID, self.postFeatured_id)
        return bool(post)

    def clickPostCommentButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonPostComment_css).click()

    def clickSignInButton(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "(//iframe[@id='comment-editor'])[1]"))
        self.driver.find_element(By.XPATH, self.buttonSignWithGoogle_css).click()
        self.driver.switch_to.default_content()

    def enterComment(self, comment):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "(//iframe[@id='comment-editor'])[1]"))
        textarea = self.driver.find_element(By.XPATH, self.textareaComment_xpath)
        textarea.send_keys(comment)

    def publishComment(self):
        self.driver.find_element(By.XPATH, self.buttonPublish_xpath).click()
        self.driver.switch_to.default_content()

    def isCommentDeleted(self):
        comments = self.driver.find_elements(By.XPATH, self.viewComments_xpath)

        for comment in comments:
            current_comment_id = comment.get_attribute("id")
            print(current_comment_id)
            if current_comment_id == self.comment_id:
                return False

        return True



