from Pages.marina_admin_page import Open_all_menus

def test_open_menus(marina_admin_login_setup):
    driver = marina_admin_login_setup
    menus = Open_all_menus(driver)
    menus.open_all_side_menus()