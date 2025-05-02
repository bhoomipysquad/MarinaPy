from Pages.redirection_flow import Redirection_Flow


def test_redirection(app_setup):
    driver = app_setup
    case1 = Redirection_Flow(driver)
    case1.direct_login()