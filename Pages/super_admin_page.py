from selenium.webdriver.common.by import By
from .base_page import BasePage


class Open_All_Menus(BasePage):

    dashboard = (By.XPATH, "//div[@title='Dashboard']//*[name()='svg']")
    map = (By.XPATH, "//div[@title='Map']//*[name()='svg']")
    marina_claims = (By.XPATH, "//ul[@role='menu']//div[@title='Marina Claims']")
    users = (By.XPATH, "//div[@title='Users']")
    Collapse_button = (By.XPATH, "//button[@type='button']")
    open_dropdown_for_logout = (By.XPATH,"//header[@class='ant-layout-header css-1wv2qmc']//div//div[@class='account-section']")
    logout = (By.XPATH, "//span[normalize-space()='Logout']")
    claim_pending = (By.XPATH, "//div[@id='rc-tabs-0-tab-pending']//div[@class='all-tab']")
    Active = (By.XPATH, "//div[@id='rc-tabs-0-tab-active']//div[@class='all-tab']")
    Inactive = (By.XPATH, "//div[@id='rc-tabs-0-tab-inactive']//div[@class='all-tab']")

    def open_all_side_menus(self):
        self.click(By.XPATH, "//button[@type='button']")
        for locator in [
            self.dashboard,
            self.map,
            self.marina_claims,
            self.Active,
            self.Inactive,
            self.claim_pending,
            self.users
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.dashboard: "https://admin-marinapy.pysquad.com/dashboard",
                self.map: "https://admin-marinapy.pysquad.com/map",
                self.marina_claims: "https://admin-marinapy.pysquad.com/marinas",
                self.Active: "https://admin-marinapy.pysquad.com/marinas",
                self.Inactive: "https://admin-marinapy.pysquad.com/marinas",
                self.claim_pending: "https://admin-marinapy.pysquad.com/marinas",
                self.users: "https://admin-marinapy.pysquad.com/settings/users",
            }
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)

        self.click(By.XPATH, "//button[@type='button']")

    def super_admin_log_out(self):
        self.click( By.XPATH,"//header[@class='ant-layout-header css-1wv2qmc']//div//div[@class='account-section']")
        self.click(By.XPATH, "//span[normalize-space()='Logout']")

        if self.driver.current_url == "https://admin-marinapy.pysquad.com/":
            pass
        else:
            self.driver.capture_screenshot("failed logout.png")
