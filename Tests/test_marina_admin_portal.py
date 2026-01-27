import time
from Pages.marina_admin_page import OpenAllMenus

def test_open_menus(marina_admin_login_via_dev_url):
    driver = marina_admin_login_via_dev_url
    menus = OpenAllMenus(driver)
    menus.open_dashboard_and_map()
    time.sleep(2)
    menus.open_my_bookings()
    time.sleep(2)
    menus.open_crm()
    time.sleep(2)
    menus.open_commerce()
    time.sleep(2)
    # menus.open_operations()
    # time.sleep(2)
    menus.open_settings()
    time.sleep(2)
    menus.open_upgrade_plans()

# def test_open_dashboard(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     dashboard = OpenAllMenus(driver)
#     dashboard.open_dashboard_and_map()
#
# def test_open_my_bookings(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     my_bookings = OpenAllMenus(driver)
#     my_bookings.open_my_bookings()
#
# def test_open_crm(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     crm = OpenAllMenus(driver)
#     crm.open_crm()
# #
# def test_open_commerce(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     commerce = OpenAllMenus(driver)
#     commerce.open_commerce()

# def test_open_operations(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     operations = OpenAllMenus(driver)
#     operations.open_operations()

# def test_open_settings(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     settings = OpenAllMenus(driver)
#     settings.open_settings()
#
# def test_open_upgrade_plans(marina_admin_login_via_dev_url):
#     driver = marina_admin_login_via_dev_url
#     plans = OpenAllMenus(driver)
#     plans.open_upgrade_plans()

