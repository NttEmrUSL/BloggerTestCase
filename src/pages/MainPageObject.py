from selenium.webdriver.common.by import By

class MainPageObject:

    buttonNewPost_css = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] div[class='Iun9']"
    buttonPost_xpath = "a[href='./blog/post/edit/2581916393429811882/7547949017194907599']"
    buttonComment_xpath = "//*[@id='yDmH0d']/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[5]/span[3]/div[2]/a"
    mainPageCheck_css = "a[id='sdgBod'] img[role='presentation']"

    def __init__(self, driver):
        self.driver = driver

    def clickNewPostButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonNewPost_css).click()

    def clickCommentButton(self):
        self.driver.find_element(By.XPATH, self.buttonComment_xpath).click()

    def mainPageCheck(self):
        if self.driver.find_element(By.CSS_SELECTOR, self.mainPageCheck_css):
            return True
        else:
            return False
