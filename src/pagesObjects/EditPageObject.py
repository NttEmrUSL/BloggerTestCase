import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class EditPageObject:

    textBoxView_xpath = "(//p)[1]"
    buttonUpdate_css = "div[aria-label='Update']"
    buttonBack_css = "div[title='Go back']"

    def __init__(self, driver):
        self.driver = driver

    #Click page you want to edit
    def clickPage(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']"))
        self.driver.find_element(By.XPATH, self.textBoxView_xpath).click()

    #Enter some text into page area
    #params string text: Edit text whatever you want
    def sendText(self, text):
        txtbox_text = self.driver.find_element(By.XPATH, self.textBoxView_xpath)
        txtbox_text.send_keys(Keys.CONTROL, Keys.END)
        pyperclip.copy(text)
        txtbox_text.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.default_content()

    #Click update button
    def clickUpdateButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonUpdate_css).click()

    #Click backpage button
    def clickBackToMainPage(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonBack_css).click()

