from selenium.webdriver.common.by import By

class LoginPageObject:

    buttonSignIn_tagname = "span"
    textBoxEmail_name = "identifier"
    buttonNextEmail_css = "#identifierNext"
    textBoxPassword_xpath = "(//input[@name='Passwd'])[1]"
    buttonNextPassword_id = "passwordNext"

    def __init__(self,driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element(By.TAG_NAME, self.buttonSignIn_tagname).click()

    def setEmail(self, email):
        emailtxt = self.driver.find_element(By.NAME, self.textBoxEmail_name)
        emailtxt.send_keys(email)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.XPATH, self.textBoxPassword_xpath)
        passwordtxt.send_keys(password)

    def clickEmailNext(self):
        self.driver.find_element(By.CSS_SELECTOR, self.buttonNextEmail_css).click()

    def clickPasswordNext(self):
        self.driver.find_element(By.ID, self.buttonNextPassword_id).click()

