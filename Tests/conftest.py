import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.login_page import LoginPage


@pytest.fixture
def super_admin_setup():
    """Setup WebDriver and login."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-marinapy.pysquad.com/")
    # Login to the application with a valid user
    login_page = LoginPage(driver)
    login_page.super_login("super-aneri@gmail.com", "SA@12345*an")
    yield driver
    driver.quit()


@pytest.fixture
def setup1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://admin-marinapy.pysquad.com/")
    yield driver
    driver.quit()

@pytest.fixture
def app_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app-marinapy.pysquad.com/")
    yield driver
    driver.quit()

@pytest.fixture
def marina_admin_login_via_dev_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://dev-marinapy.pysquad.com/")
    login = LoginPage(driver)
    assert  driver.current_url == "https://dev-marinapy.pysquad.com/"
    time.sleep(1)
    login.click(By.XPATH,"//span[normalize-space()='Login']")
    time.sleep(1)
    assert driver.current_url == "https://dev-marinapy.pysquad.com/login"
    time.sleep(1)
    login.click(By.XPATH ,"//input[@id='email']")
    login.send_keys(By.XPATH, "//input[@id='email']","bhoomi+finalbookinadmin@pysquad.com")
    time.sleep(1)
    login.click(By.XPATH ,"//input[@id='password']")
    login.send_keys(By.XPATH,"//input[@id='password']","bhumiB2111@")
    time.sleep(1)
    login.click(By.XPATH ,"//span[normalize-space()='Login']")
    time.sleep(2)
    login.click(By.XPATH , "//input[@aria-label='OTP Input 1']")
    assert driver.current_url == "https://dev-marinapy.pysquad.com/otp"
    login.send_keys(By.XPATH, "//input[@aria-label='OTP Input 1']", "1")
    login.send_keys(By.XPATH , "//input[@aria-label='OTP Input 2']" ,"2")
    login.send_keys(By.XPATH , "//input[@aria-label='OTP Input 3']" ,"3")
    login.send_keys(By.XPATH , "//input[@aria-label='OTP Input 4']" ,"4")
    login.send_keys(By.XPATH , "//input[@aria-label='OTP Input 5']" ,"5")
    login.send_keys(By.XPATH , "//input[@aria-label='OTP Input 6']" ,"6")
    time.sleep(10)
    assert driver.current_url == "https://app-marinapy.pysquad.com/dashboard"
    yield driver
    driver.quit()


@pytest.fixture
def marina_admin_login_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app-marinapy.pysquad.com/")
    login_page = LoginPage(driver)
    login_page.login("bhoomi+finalbookinadmin@pysquad.com", "bhumiB2111@")
    # login_page.click(By.XPATH , "//input[@aria-label='OTP Input 1']")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 1']" ,"1")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 2']" ,"2")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 3']" ,"3")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 4']" ,"4")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 5']" ,"5")
    # login_page.send_keys(By.XPATH , "//input[@aria-label='OTP Input 6']" ,"6")
    yield driver
    driver.quit()
