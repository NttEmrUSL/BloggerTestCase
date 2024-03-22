from selenium.webdriver.common.by import By

class MainPageObject:

    buttonNewPost_css = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] div[class='Iun9']"
    buttonPost_xpath = "(//a)[40]"
    buttonComment_xpath = "//*[@id='yDmH0d']/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[5]/span[3]/div[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def clickNewPostButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonNewPost_css).click()

    def clickPostButton(self):
        self.driver.find_element(By.XPATH, self.buttonPost_xpath).click()

    def clickCommentButton(self):
        self.driver.find_element(By.XPATH, self.buttonComment_xpath).click()


