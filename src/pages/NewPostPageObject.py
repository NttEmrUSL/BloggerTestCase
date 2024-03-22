import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class NewPostPageObject:
    buttonInsertImage_css = "(//span[contains(@class,'DPvwYc sm8sCf GHpiyd')][contains(text(),'')])[1]"
    buttonInsertByUrl_css = "div[class='JPdR6b e5Emjc qjTEB'] span[aria-label='By URL']"
    textBoxUrl_css = "input[id=':c']"
    buttonSelect_id = "picker:ap:0"
    buttonPublish_css = "div[aria-label='Publish'] span[class='CwaK9']"
    buttonConfirm_xpath = "/html[1]/body[1]/div[7]/div[4]/div[1]/div[2]/div[3]/div[2]/span[1]/span[1]"
    newPostPageCheck_css = "div[aria-label='Publish'] span[class='CwaK9']"

    def __init__(self, driver):
        self.driver = driver

    def newPostPageCheck(self):
        if self.driver.find_element(By.CSS_SELECTOR, self.newPostPageCheck_css):
            return True
        else:
            return False

    def clickInsertImage(self):
        self.driver.find_element(By.XPATH, self.buttonInsertImage_css).click()

    def clickAddByUrl(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonInsertByUrl_css).click()

    def setImageUrl(self, url):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        txtbox_url = self.driver.find_element(By.CSS_SELECTOR, self.textBoxUrl_css)
        pyperclip.copy(url)
        txtbox_url.send_keys(Keys.CONTROL, 'v')

    def clickSelect(self):
        self.driver.find_element(By.ID, self.buttonSelect_id).click()
        self.driver.switch_to.default_content()

    def clickPublish(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonPublish_css).click()

    def clickConfirm(self):
        self.driver.find_element(By.XPATH, self.buttonConfirm_xpath).click()