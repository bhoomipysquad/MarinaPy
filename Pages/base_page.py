from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()
        time.sleep(1)

    def send_keys(self, by, value, text):
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)
        time.sleep(1)

    def capture_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

