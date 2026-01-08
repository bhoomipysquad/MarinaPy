import time
from selenium.webdriver.common.by import By
from .base_page import BasePage


class OpenAllMenus(BasePage):

    MENU = {
        "Dashboard": ((By.XPATH, "//ul[@role='menu']//div[@title='Dashboard']"), "https://app-marinapy.pysquad.com/dashboard"),
        "Map": ((By.XPATH, "//ul[@role='menu']//div[@title='Map']"),"https://app-marinapy.pysquad.com/map"),
        "Berths": ((By.XPATH, "//span[normalize-space()='Berths']"),  "https://app-marinapy.pysquad.com/booking/berth-listing"),
        "My Bookings": ((By.XPATH, "//span[normalize-space()='My Bookings']"), "https://app-marinapy.pysquad.com/booking/my-bookings"),
        "Clients": ((By.XPATH, "//span[normalize-space()='Clients']"), "https://app-marinapy.pysquad.com/crm/clients"),
        "Boats": ((By.XPATH, "//span[normalize-space()='Boats']"), "https://app-marinapy.pysquad.com/crm/boats"),
        "Waiting List": ((By.XPATH, "//span[normalize-space()='Waiting List']"), "https://app-marinapy.pysquad.com/waiting-list"),
        "Quotes": ((By.XPATH, "//span[normalize-space()='Quotes']"), "https://app-marinapy.pysquad.com/commerce/quote"),
        "Invoices": ((By.XPATH, "//span[normalize-space()='Invoices']"), "https://app-marinapy.pysquad.com/commerce/invoice"),
        "Payments": ((By.XPATH, "//span[normalize-space()='Payments']"), "https://app-marinapy.pysquad.com/commerce/payment"),
        # "Request" : ((By.XPATH,"//li[@role='none']//span[@class='ant-menu-title-content'][normalize-space()='Request']") , "https://app-marinapy.pysquad.com/operations/request"),
        # "Services": ((By.XPATH ,"//li[@role='none']//span[@class='ant-menu-title-content'][normalize-space()='Services']") , "https://app-marinapy.pysquad.com/operations/services"),
        "My Marina": ((By.XPATH, "//span[normalize-space()='My Marina']"),  "https://app-marinapy.pysquad.com/settings/marina-profile"),
        "Users": ((By.XPATH, "//span[normalize-space()='Users']"),"https://app-marinapy.pysquad.com/settings/users"),
        "Catalog": ((By.XPATH, "//span[normalize-space()='Catalog']"),"https://app-marinapy.pysquad.com/settings/catalog"),
        "Import Data": ((By.XPATH, "//span[normalize-space()='Import Data']"), "https://app-marinapy.pysquad.com/settings/import-data"),
        "Communication": ((By.XPATH, "//span[normalize-space()='Communication']"),"https://app-marinapy.pysquad.com/settings/communication"),
        "Subscription": ((By.XPATH, "//span[normalize-space()='Subscription']"), "https://app-marinapy.pysquad.com/upgrade-plans/plans"),
        "Billings": ((By.XPATH, "//span[normalize-space()='Billings']"), "https://app-marinapy.pysquad.com/upgrade-plans/billings")
    }

    def open_menu(self, hover_xpath, menu_keys):
        self.hover_event(By.XPATH, hover_xpath)
        for key in menu_keys:
            locator, expected_url = self.MENU[key]
            self.click(*locator)
            self.scroll_up_down()
            assert self.driver.current_url == expected_url, \
                f"URL mismatch: {self.driver.current_url}"
            self.hover_event(By.XPATH, hover_xpath)
            time.sleep(1)

    def open_dashboard_and_map(self):
        self.open_menu("//button[@type='button']", ["Dashboard", "Map"])

    def open_my_bookings(self):
        self.open_menu("//li[1]//div[1]", ["Berths", "My Bookings"])

    def open_crm(self):
        self.open_menu("//li[2]//div[1]", ["Clients", "Boats", "Waiting List"])

    def open_commerce(self):
        self.open_menu("//li[3]//div[1]//i[1]", ["Quotes", "Invoices", "Payments"])

    # def open_operations(self):
    #     self.open_menu("//li[4]//div[1]" , ["Request" , "Services"])

    def open_settings(self):
        self.open_menu("//li[4]//div[1]",  ["My Marina", "Users", "Catalog", "Import Data", "Communication"])

    def open_upgrade_plans(self):
        self.open_menu("//li[5]//div[1]", ["Subscription", "Billings"])





















































# import time
# from selenium.webdriver.common.by import By
# from .base_page import BasePage
#
#
#
# class Open_all_menus(BasePage):
#     collapse_button = (By.XPATH , "//button[@type='button']")
#     Map = (By.XPATH ,"//ul[@role='menu']//div[@title='Map']")
#     Berths = (By.XPATH, "//span[normalize-space()='Berths']")
#     My_bookings = (By.XPATH, "//span[normalize-space()='My Bookings']")
#     Clients = (By.XPATH, "//span[normalize-space()='Clients']")
#     Boats = (By.XPATH, "//span[normalize-space()='Boats']")
#     Waiting_list = (By.XPATH, "//span[normalize-space()='Waiting List']")
#     Quotes = (By.XPATH, "//span[normalize-space()='Quotes']")
#     Invoices = (By.XPATH ,"//span[normalize-space()='Invoices']")
#     Payments = (By.XPATH ,"//span[normalize-space()='Payments']")
#     My_marina = (By.XPATH, "//span[normalize-space()='My Marina']")
#     Users = (By.XPATH, "//span[normalize-space()='Users']")
#     Catalog = (By.XPATH, "//span[normalize-space()='Catalog']")
#     Import_data = (By.XPATH, "//span[normalize-space()='Import Data']")
#     Communication = (By.XPATH, "//span[normalize-space()='Communication']")
#     Subscription = (By.XPATH, "//span[normalize-space()='Subscription']")
#     Billings = (By.XPATH, "//span[normalize-space()='Billings']")
#     Dashboard= (By.XPATH ,"//ul[@role='menu']//div[@title='Dashboard']")
#
#
#     def open_dashboard_and_map(self):
#         self.click(By.XPATH ,"//button[@type='button']")
#         time.sleep(1)
#         for locator in [
#            self.Dashboard, self.Map
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.Map : "https://app-marinapy.pysquad.com/map" ,
#                 self.Dashboard: "https://app-marinapy.pysquad.com/dashboard"}
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#         self.click(By.XPATH ,"//button[@type='button']")
#
#
#     def open_my_bookings(self):
#         self.hover_event(By.XPATH ,"//li[1]//div[1]")    #My bookings
#         for locator in [
#             self.Berths, self.My_bookings
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.Berths: "https://app-marinapy.pysquad.com/booking/berth-listing",
#                 self.My_bookings: "https://app-marinapy.pysquad.com/booking/my-bookings"}
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#             self.hover_event(By.XPATH, "//li[1]//div[1]")
#
#     def open_crm(self):
#         self.hover_event(By.XPATH , "//li[2]//div[1]")    # CRM
#         for locator in [
#             self.Clients, self.Boats ,self.Waiting_list
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.Clients: "https://app-marinapy.pysquad.com/crm/clients",
#                 self.Boats: "https://app-marinapy.pysquad.com/crm/boats",
#                 self.Waiting_list: "https://app-marinapy.pysquad.com/waiting-list"}
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#             self.hover_event(By.XPATH, "//li[2]//div[1]")
#
#     def open_commerce(self):
#         self.hover_event(By.XPATH , "//li[3]//div[1]//i[1]")  #Commerce
#         for locator in [
#             self.Quotes, self.Invoices ,self.Payments
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.Quotes: "https://app-marinapy.pysquad.com/commerce/quote",
#                 self.Invoices: "https://app-marinapy.pysquad.com/commerce/invoice",
#                 self.Payments: "https://app-marinapy.pysquad.com/commerce/payment",}
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#             time.sleep(2)
#             self.hover_event(By.XPATH, "//li[3]//div[1]//i[1]")
#
#     def open_settings(self):
#         self.hover_event(By.XPATH , "//li[4]//div[1]")  #settings
#         for locator in [
#             self.My_marina, self.Users, self.Catalog,self.Import_data,self.Communication
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.My_marina: "https://app-marinapy.pysquad.com/settings/marina-profile",
#                 self.Users: "https://app-marinapy.pysquad.com/settings/users",
#                 self.Catalog: "https://app-marinapy.pysquad.com/settings/catalog",
#                 self.Import_data: "https://app-marinapy.pysquad.com/settings/import-data",
#                 self.Communication: "https://app-marinapy.pysquad.com/settings/communication" }
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#             time.sleep(2)
#             self.hover_event(By.XPATH, "//li[4]//div[1]")
#
#     def open_upgrade_plans(self):
#         self.hover_event(By.XPATH , "//li[5]//div[1]")
#         for locator in [
#             self.Subscription, self.Billings
#         ]:
#             self.click(*locator)
#             self.scroll_up_down()
#             url_map = {
#                 self.Subscription: "https://app-marinapy.pysquad.com/upgrade-plans/plans",
#                 self.Billings: "https://app-marinapy.pysquad.com/upgrade-plans/billings"}
#             print(self.driver.current_url)
#             assert self.driver.current_url == url_map.get(locator)
#             if self.driver.current_url != url_map.get(locator):
#                 print(self.driver.current_url)
#             time.sleep(2)
#             self.hover_event(By.XPATH, "//li[5]//div[1]")
#
#
#
#
#
#
#
#
