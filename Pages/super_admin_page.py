from selenium.webdriver.common.by import By
from .base_page import BasePage

class Open_All_Menus(BasePage):
    dashboard = (By.XPATH , "//div[@title='Dashboard']//*[name()='svg']")
    map = (By.XPATH , "//div[@title='Map']//*[name()='svg']")
    marina_claims = (By.XPATH , "//div[@title='Marina claims']")
    billing = (By.XPATH , "//div[@title='Billing']")
    users = (By.XPATH , "//div[@title='Users']")
    settings = (By.XPATH , "//div[@title='Settings']")
    Collapse_button = (By.XPATH , "//button[@type='button']")
    open_dropdown_for_logout = (By.XPATH ,"//span[normalize-space()='Admin']")
    logout = (By.XPATH , "//span[normalize-space()='Logout']")


    def open_all_side_menus(self):
        for locator in [self.map, self.dashboard,self.marina_claims,
                        self.billing,self.users,self.settings]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {   self.map: "https://admin-marinapy.pysquad.com/map",
                          self.dashboard: "https://admin-marinapy.pysquad.com/dashboard",
                          self.marina_claims: "https://admin-marinapy.pysquad.com/marinas",
                          self.billing: "https://admin-marinapy.pysquad.com/billing",
                          self.users: "https://admin-marinapy.pysquad.com/users",
                          self.settings: "https://admin-marinapy.pysquad.com/settings"
                      }
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)

        self.click(By.XPATH, "//button[@type='button']")
        self.click(By.XPATH, "//button[@type='button']")

    def super_admin_log_out(self):
        self.click(By.XPATH , "//span[normalize-space()='Admin']")
        self.click(By.XPATH, "//span[normalize-space()='Logout']")
        if self.driver.current_url == "https://admin-marinapy.pysquad.com/":
            pass
        else:
            self.driver.capture_screenshot("failed logout.png")
