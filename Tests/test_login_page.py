import time
import pytest
from Pages.login_page import LoginPage

# login with valid--invalid inputs in superadmin and marina admin side......create new user


@pytest.mark.parametrize("username,password", [("manju.pysquad@gmail.com", "User@1234"),
                                               ("bhoomi+techno@pysquad.com" , "bhumiB2111@"),
                                               ("super-aneri@gmail.com", "SA@12345*an")])
def test_super_admin_login_with_valid_invalid_inputs(setup1,username,password):
    driver = setup1
    login_page = LoginPage(driver)
    login_page.super_login(username,password)
    time.sleep(2)

    current_url = driver.current_url
    print("Current URL is ----> ", current_url)

    if username == "super-aneri@gmail.com" and password == "SA@12345*an":
        if current_url != "https://admin-marinapy.pysquad.com/dashboard":
            driver.save_screenshot("failed_valid_login.png")
            assert False, "Valid credentials failed to login"
    else:
        if current_url == "https://admin-marinapy.pysquad.com/dashboard":
            driver.save_screenshot("invalid_login_allowed.png")
            assert False, "Invalid credentials should not allow dashboard access"






@pytest.mark.parametrize("username,password", [("manju.pysquad@gmail.com", "User@1234"),
                                               ("super-aneri@gmail.com", "SA@12345*an")])
def test_marina_admin_login_with_valid_invalid_inputs(app_setup,username,password):
    driver = app_setup
    login_page = LoginPage(driver)
    login_page.login_marina_admin(username, password)
    time.sleep(2)

    current_url = driver.current_url
    print("Current URL is ---->", current_url)
    valid_url = "https://app-marinapy.pysquad.com/claim"

    if username == "super-aneri@gmail.com" and password == "SA@12345*an":
        if current_url == valid_url:
            driver.save_screenshot("failed_marina_admin_valid_login.png")
            assert False, f"Expected valid login to redirect to {valid_url}, but got {current_url}"
    else:
        if current_url == valid_url:
            driver.save_screenshot("failed_marina_admin_invalid_login.png")
            assert False, f"Invalid credentials incorrectly allowed access to {valid_url}"






def test_super_admin_login_with_valid_inputs(setup1):
    driver = setup1
    login_super_admin = LoginPage(driver)
    login_super_admin.super_login("super-aneri@gmail.com" , "SA@12345*an")
    time.sleep(2)
    assert driver.current_url == "https://admin-marinapy.pysquad.com/dashboard"






def test_registration_with_valid_inputs(app_setup):
    driver = app_setup
    create_user = LoginPage(driver)
    create_user.create_new_account("priyanka", "rai","bhoomi+ati90i@pysquad.com","jk6786H&**")






def test_marina_admin_login_with_valid_inputs(app_setup):
    driver = app_setup
    login_admin = LoginPage(driver)
    login_admin.login_marina_admin("manju.pysquad@gmail.com" , "User@1234")
    time.sleep(2)
    assert driver.current_url == "https://app-marinapy.pysquad.com/map"

