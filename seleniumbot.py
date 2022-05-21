from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element(by=By.CSS_SELECTOR,
                                                   value="input[name='username']")
        password_input = self.browser.find_element(by=By.CSS_SELECTOR,
                                                   value="input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element(by=By.XPATH, value="//button[@type='submit']")
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        return LoginPage(self.browser)

def test_login_page():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome("/Users/berkealtiparmak/Desktop/InstagramBot/chromedriver",
                               options=chrome_options)
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    username = input("enter username")
    password = input("enter password")
    login_page.login(username, password)

    errors = browser.find_elements(by=By.CSS_SELECTOR, value='#error_message')
    assert len(errors) == 0
