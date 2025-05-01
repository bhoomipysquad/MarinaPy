import time
import pytest
from Pages.login_page import LoginPage

credentials = [
                  ("bhoomi+techno@pysquad.com", "bhumiB2111@"),
                  ("manju.pysquad@gmail.com", "User@1234"),
                  ("super-aneri@gmail.com", "SA@12345*an")
              ]

@pytest.mark.parametrize("username,password", credentials)
def test_super_admin_login_with_valid_invalid_inputs(setup1,username,password):
    driver = setup1
    login_page = LoginPage(driver)
    login_page.login(username,password)

    if username == "super-aneri@gmail.com" and password == "SA@12345*an":
        print("current url is ---->   ", driver.current_url)
        time.sleep(2)
        if driver.current_url == "https://admin-marinapy.pysquad.com/dashboard":
            pass
        else:
            driver.capture_screenshot("failed super admin username.png")

    elif username != "super-aneri@gmail.com" and password != "SA@12345*an":
        print("current url is ---->   ", driver.current_url)
        if driver.current_url == "https://admin-marinapy.pysquad.com":
            pass
    else:
            driver.capture_screenshot("failed super admin username.png")



@pytest.mark.parametrize("username,password", credentials)
def test_marina_admin_login_with_valid_invalid_inputs(setup2,username,password):
    driver = setup2
    login_page = LoginPage(driver)
    login_page.login_marina_admin(username, password)

    if username == "super-aneri@gmail.com" and password == "SA@12345*an":
        print("current url is ---->   ", driver.current_url)
        if driver.current_url != "https://app-marinapy.pysquad.com":
            pass
        else:
            driver.capture_screenshot("failed marina admin username.png")

    elif username != "super-aneri@gmail.com" and password != "SA@12345*an":
        print("current url is ---->   ", driver.current_url)
        if driver.current_url == "https://app-marinapy.pysquad.com/claim":
            pass
    else:
        driver.capture_screenshot("failed marina admin username.png")



def test_registration_with_valid_invalid_inputs(app_setup):
    driver = app_setup
    create_user = LoginPage(driver)
    create_user.create_new_account("priyanka", "rai","bhoomi+ati90i@pysquad.com","jk6786H&**")
