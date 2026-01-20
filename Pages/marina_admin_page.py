import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class OpenAllMenus(BasePage):
    collapse_button = (By.XPATH , "//button[@type='button']")
    Map = (By.XPATH ,"//ul[@role='menu']//div[@title='Map']")
    Berths = (By.XPATH, "//span[normalize-space()='Berths']")
    Inactive = (By.XPATH, "//div[@class='ant-tabs-tab ant-tabs-tab-active']")
    Active = (By.XPATH, "//div[@data-node-key='Active']")
    Rented = (By.XPATH, "//div[@data-node-key='Rented']")
    Available = (By.XPATH, "//div[@data-node-key='Rented']")
    Boat_present = (By.XPATH, "//div[@data-node-key='boat_present']")
    Boat_absent = (By.XPATH, "//div[@data-node-key='boat_absent']")
    Stopover = (By.XPATH, "//div[@data-node-key='stopover']")
    Permanent = (By.XPATH, "//div[@data-node-key='permanent']")
    My_bookings = (By.XPATH, "//span[normalize-space()='My Bookings']")
    Clients = (By.XPATH, "//span[normalize-space()='Clients']")
    Boats = (By.XPATH, "//span[normalize-space()='Boats']")
    Waiting_list = (By.XPATH, "//span[normalize-space()='Waiting List']")
    Quotes = (By.XPATH, "//span[normalize-space()='Quotes']")
    Invoices = (By.XPATH ,"//span[normalize-space()='Invoices']")
    Payments = (By.XPATH ,"//span[normalize-space()='Payments']")
    My_marina = (By.XPATH, "//span[normalize-space()='My Marina']")
    Users = (By.XPATH, "//span[normalize-space()='Users']")
    Catalog = (By.XPATH, "//span[normalize-space()='Catalog']")
    Import_data = (By.XPATH, "//span[normalize-space()='Import Data']")
    Communication = (By.XPATH, "//span[normalize-space()='Communication']")
    Subscription = (By.XPATH, "//span[normalize-space()='Subscription']")
    Billings = (By.XPATH, "//span[normalize-space()='Billings']")
    Dashboard= (By.XPATH ,"//ul[@role='menu']//div[@title='Dashboard']")


    def open_dashboard_and_map(self):
        self.click(*self.collapse_button)
        time.sleep(1)
        for locator in [
           self.Dashboard, self.Map
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.Map : "https://app-marinapy.pysquad.com/map" ,
                self.Dashboard: "https://app-marinapy.pysquad.com/dashboard"}
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
        self.click(*self.collapse_button)


    def open_my_bookings(self):
        self.hover_event(By.XPATH ,"//li[1]//div[1]")    #My bookings
        for locator in [self.Berths, self.My_bookings]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.Berths: "https://app-marinapy.pysquad.com/booking/berth-listing",
                self.My_bookings: "https://app-marinapy.pysquad.com/booking/my-bookings"}
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
            self.hover_event(By.XPATH, "//li[1]//div[1]")
        self.click(*self.Berths)
        filters = {
            self.Inactive: "Inactive",
            self.Active: "Active",
            self.Rented: "Rented",
            self.Available: "Available",
            self.Boat_present: "Boat Present",
            self.Boat_absent: "Boat Absent",
            self.Stopover: "Stopover",
            self.Permanent: "Permanent"
        }

        for locator, expected_text in filters.items():
            self.click(*locator)
            self.scroll_up_down()
            is_visible = self.is_text_visible(expected_text)
            assert is_visible, f"Expected text not visible on screen: {expected_text}"

    def open_crm(self):
        self.hover_event(By.XPATH , "//li[2]//div[1]")    # CRM
        for locator in [
            self.Clients, self.Boats ,self.Waiting_list
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.Clients: "https://app-marinapy.pysquad.com/crm/clients",
                self.Boats: "https://app-marinapy.pysquad.com/crm/boats",
                self.Waiting_list: "https://app-marinapy.pysquad.com/waiting-list"}
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
            self.hover_event(By.XPATH, "//li[2]//div[1]")

    def open_commerce(self):
        self.hover_event(By.XPATH , "//li[3]//div[1]//i[1]")  #Commerce
        for locator in [
            self.Quotes, self.Invoices ,self.Payments
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.Quotes: "https://app-marinapy.pysquad.com/commerce/quote",
                self.Invoices: "https://app-marinapy.pysquad.com/commerce/invoice",
                self.Payments: "https://app-marinapy.pysquad.com/commerce/payment",}
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
            time.sleep(2)
            self.hover_event(By.XPATH, "//li[3]//div[1]//i[1]")

    def open_settings(self):
        self.hover_event(By.XPATH , "//li[4]//div[1]")  #settings
        for locator in [
            self.My_marina, self.Users, self.Catalog,self.Import_data,self.Communication
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.My_marina: "https://app-marinapy.pysquad.com/settings/marina-profile",
                self.Users: "https://app-marinapy.pysquad.com/settings/users",
                self.Catalog: "https://app-marinapy.pysquad.com/settings/catalog",
                self.Import_data: "https://app-marinapy.pysquad.com/settings/import-data",
                self.Communication: "https://app-marinapy.pysquad.com/settings/communication" }
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
            time.sleep(2)
            self.hover_event(By.XPATH, "//li[4]//div[1]")

    def open_upgrade_plans(self):
        self.hover_event(By.XPATH , "//li[5]//div[1]")
        for locator in [
            self.Subscription, self.Billings
        ]:
            self.click(*locator)
            self.scroll_up_down()
            url_map = {
                self.Subscription: "https://app-marinapy.pysquad.com/upgrade-plans/plans",
                self.Billings: "https://app-marinapy.pysquad.com/upgrade-plans/billings"}
            print(self.driver.current_url)
            assert self.driver.current_url == url_map.get(locator)
            if self.driver.current_url != url_map.get(locator):
                print(self.driver.current_url)
            time.sleep(2)
            self.hover_event(By.XPATH, "//li[5]//div[1]")

