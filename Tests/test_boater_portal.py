from Pages.boater_add_new_boat import Add_new_boat
from Pages.boater_booking_flow import Boater_Booking

def test_boater_booking_flow(boater_acc_login):
    driver = boater_acc_login
    booking = Boater_Booking(driver)
    booking.booking_by_boater()


def test_add_new_boat(boater_acc_login):
    driver = boater_acc_login
    add_boat = Add_new_boat(driver)
    add_boat.add_new_boat()
