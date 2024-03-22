import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class EditPageObject:

    textBoxView_xpath = "(//p)[1]"
    buttonUpdate_css = "div[aria-label='Update']"
    buttonBack_css = "div[title='Go back']"

    def __init__(self, driver):
        self.driver = driver


    def clickPage(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']"))
        self.driver.find_element(By.XPATH, self.textBoxView_xpath).click()

    def sendText(self, text):
        txtbox_text = self.driver.find_element(By.XPATH, self.textBoxView_xpath)
        txtbox_text.send_keys(Keys.CONTROL, Keys.END)
        pyperclip.copy(text)
        txtbox_text.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.default_content()

    def clickUpdateButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonUpdate_css).click()

    def clickBackToMainPage(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonBack_css).click()

