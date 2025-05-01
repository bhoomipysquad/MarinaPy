from Pages.super_admin_page import Open_All_Menus

def test_open_menus(super_admin_setup):
    driver = super_admin_setup
    menus = Open_All_Menus(driver)
    menus.open_all_side_menus()
    menus.super_admin_log_out()

