import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Boater_Booking(BasePage):
    search_marina = (By.XPATH, '//span[2]')
    search_placeholder = (By.XPATH, "//input[@placeholder='Search Marina Name and Id']" , "Search Marina Name and Id")
    search_button = (By.XPATH, "//span[normalize-space()='Search']")
    marina_name = (By.XPATH , "//input[@placeholder='Search Marina Name and Id']" , "550 Marina")
    click_marina = (By.XPATH, "//h6[normalize-space()='Marina Id : 7593']")
    marina_url = "https://dev-marinapy.pysquad.com/open/marinas/550-marina-in-united-states"
    book_a_slip =  (By.XPATH , "//span[normalize-space()='Book a Slip']")
    first_name = (By.XPATH , "//input[@id='first_name']")
    last_name = (By.XPATH , "//input[@id='last_name']")
    email = (By.XPATH , "//input[@id='email']")
    address = (By.XPATH , "//input[@id='address']")
    state = ()
    city = ()
    postal_code = ()
    confirm_booking_button = (By.XPATH, "//button[@type='submit']")
    back_to_bookings = (By.XPATH , "//span[normalize-space()='Back to my bookings']")
    #Boat Information
    select_boat_field = (By.XPATH , "//input[@id='selectedBoat']")
    boat_name  = (By.XPATH , "//input[@id='selectedBoat']", "boat test 3" )
    #Date info
    arrival  = (By.XPATH , "//input[@id='arrival']")
    arrival_date_data = (By.XPATH , "//input[@id='arrival']" , "20-04-2026 / 04:05 PM")
    Departure = (By.XPATH , "//input[@id='departure']")
    Departure_date_data = (By.XPATH , "//input[@id='departure']" , "22-04-2026 / 04:05 PM")
    permanent_book  = (By.XPATH , "//span[contains(text(),'Book Permanent Berth')]")


    def booking_by_boater(self):
        self.click(*self.search_marina)
        self.assert_placeholder(*self.search_placeholder)
        self.send_keys(*self.marina_name)
        self.click(*self.search_button)
        self.click(*self.click_marina)
        self.scroll_up_down_by_pixel()
        self.windows_and_scroll()
        print(self.get_current_url())
        assert self.get_current_url() == self.marina_url, "Marina page not opened"
        if self.get_current_url() == self.marina_url:
            self.click(*self.book_a_slip)
        else:
            print(self.get_current_url())
            self.save_screenshot("booking form not opened.png")
        time.sleep(2)
        assert self.get_current_url() == "https://dev-marinapy.pysquad.com/quote-request" , "Booking page not opened"
        for field in (self.first_name,self.last_name,self.email,self.address):
            self.click(*field)
        self.scroll_up_down_with_element(By.XPATH, "//button[@type='submit']")
        self.click(*self.select_boat_field)
        self.send_keys(*self.boat_name)
        self.tab_keys(*self.select_boat_field)
        self.click(*self.arrival)
        self.send_keys(*self.arrival_date_data)
        self.tab_keys(*self.arrival)
        self.click(*self.Departure)
        self.send_keys(*self.Departure_date_data)
        self.tab_keys(*self.Departure)
        # self.click(*self.permanent_book)
        self.click(*self.confirm_booking_button)
        if self.is_text_visible("Your Request Is on Its Way"):
            self.click(*self.back_to_bookings)
            assert self.get_current_url() ==  "https://dev-marinapy.pysquad.com/booking/stopover"
        else:
            self.save_screenshot("booking failed.png")
            assert False, "Booking confirmation not shown"