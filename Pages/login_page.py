import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.ID, "email")
    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    click_on_profile_app = (By.XPATH , "//span[@class='ant-avatar ant-avatar-lg ant-avatar-circle css-uzzqyd']")
    click_login_to_open_login_page_app = (By.XPATH , "//span[@class='ant-typography css-uzzqyd']")
    create_one = (By.XPATH , "//span[normalize-space()='Create One']")
    first_name = (By.XPATH , "//input[@id='first_name']")
    last_name = (By.XPATH , "//input[@id='last_name']")
    email_field = (By.ID , "email")
    create_password_field = (By.ID , "password1")
    click_create_account = (By.XPATH , "//span[normalize-space()='Create account']")

    def enter_username(self, username):
        self.send_keys(By.ID, "email" , username)

    def enter_password(self, password):
        self.send_keys(By.ID, "password" , password)

    def click_login(self):
        self.click(By.XPATH, "//button[@type='submit']")

    def click_profile_app(self):
        self.click(By.XPATH,"//span[@class='ant-avatar ant-avatar-lg ant-avatar-circle css-uzzqyd']")
        self.click(By.XPATH , "//span[@class='ant-typography css-uzzqyd']")

    def click_on_create_user(self):
        self.click(By.XPATH , "//span[normalize-space()='Create One']")

    def enter_data_to_create_new_account(self , fname ,lname , emailid , new_password):
        for by, locator, value in [
            (By.ID, "first_name", fname),
            (By.ID, "last_name", lname),
            (By.ID, "email", emailid),
            (By.ID, "password1", new_password),
        ]:
            self.click(by, locator)
            self.send_keys(by, locator, value)

    def click_to_make_new_user(self):
        self.click(By.XPATH , "//span[normalize-space()='Create account']")
        time.sleep(2)


    def login(self, username, password):
        """Log in using provided username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(2)

    def login_marina_admin (self , username ,password ):
        self.click_profile_app()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def create_new_account (self, fname ,lname , emailid , new_password):
        self.click_profile_app()
        self.click_on_create_user()
        self.enter_data_to_create_new_account(fname ,lname , emailid , new_password)
        self.click_to_make_new_user()



