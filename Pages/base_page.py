from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def hover_event(self, by, value):
        tooltip_element = self.driver.find_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(tooltip_element).perform()  # Hover over element
        time.sleep(2)  # Wait so you can see the tooltip


