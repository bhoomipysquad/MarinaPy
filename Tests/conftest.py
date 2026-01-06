import pytest
from selenium import webdriver
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
def marina_admin_login_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app-marinapy.pysquad.com/")
    login_page = LoginPage(driver)
    login_page.login("bhoomi+finalbookinadmin@pysquad.com", "bhumiB2111@")
    yield driver
    driver.quit()
