import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Claim_Marina(BasePage):
    search_marina = (By.XPATH, '//span[2]')
    search_placeholder = (By.XPATH, "//input[@placeholder='Search Marina Name and Id']" , "Search Marina Name and Id")
    search_button = (By.XPATH, "//span[normalize-space()='Search']")
    marina_name = (By.XPATH , "//input[@placeholder='Search Marina Name and Id']" , "2")
    click_marina = (By.XPATH , "//h6[normalize-space()='Marina Id : 2']")
    marina_url = "https://dev-marinapy.pysquad.com/open/marinas/crabbs-slipway-marina-in-antigua-and-barbuda"
    visible_text = "Crabb's Slipway Marina"

    def claim_marina_flow(self):
        self.click(*self.search_marina)
        self.assert_placeholder(*self.search_placeholder)
        self.send_keys(*self.marina_name)
        self.click(*self.search_button)
        self.click(*self.click_marina)
        time.sleep(3)
        print(self.get_current_url())
        assert self.get_current_url() == self.marina_url
        assert self.is_text_visible(*self.visible_text)
        time.sleep(10)






