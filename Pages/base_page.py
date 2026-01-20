from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
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

    def send_keys1(self, locator, text):
        by , value = locator
        self.wait_for_element(by, value)
        element = self.driver.find_element(by, value)
        element.send_keys(text)

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def scroll_up_down_with_element(self,by, value):
        element = self.driver.find_element(by ,value)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

    def hover_event(self, by, value):
        tooltip_element = self.driver.find_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(tooltip_element).perform()  # Hover over element
        time.sleep(2)  # Wait so you can see the tooltip

    def is_text_visible(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located( ("xpath", f"//*[contains(text(), '{text}')]") ))
            return True
        except TimeoutException:
            return False

    def assert_placeholder(self, by, value, expected_placeholder):
        element = self.driver.find_element(by, value)
        self.wait_for_element(by, value)
        actual_placeholder = element.get_attribute("placeholder")
        assert actual_placeholder == expected_placeholder, (
            f"Expected placeholder '{expected_placeholder}', "f"but got '{actual_placeholder}'")


    def scroll_up_down_by_pixel(self):
        for i in range(5):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(0.5)
        time.sleep(3)
        for i in range(5):
            self.driver.execute_script("window.scrollBy(0, -500);")
            time.sleep(0.5)

    def get_current_url(self):
        return self.driver.current_url

    def windows_and_scroll(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.scroll_up_down_by_pixel()

    def tab_keys(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.TAB)
        time.sleep(2)

    def enter_key(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.ENTER)
        time.sleep(2)

    def down_key(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)

    def upload_file(self, locator, file_path):
        by,value = locator
        file_input = self.driver.find_element(by, value)
        file_input.send_keys(file_path)

    def switch_to_iframe(self, by, value):
        iframe = self.driver.find_element(by, value)
        self.driver.switch_to.frame(iframe)

