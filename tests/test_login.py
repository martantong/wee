import allure

from pages.login import LoginDialog
from pages.main import MainPage


def test_login(browser):
    main_page = MainPage(browser)

    with allure.step("Click 'Profile' button"):
        main_page.open_login_form()

    with allure.step("Check that 'Log in' dialog is opened"):
        login_dialog = LoginDialog(browser)
        assert login_dialog.hello_message.is_displayed(), "'Log in' dialog is not displayed"

    with allure.step("Select country code"):
        login_dialog.select_country_code("Russian Federation")

    with allure.step("Input phone"):
        login_dialog.input_phone("1234567890")

    with allure.step("Check that 'Log in' button is enabled"):
        login_dialog = LoginDialog(browser)
        assert login_dialog.login_button.is_displayed(), "'Log in' button is disabled"

    with allure.step("Click 'Lig in' button"):
        login_dialog.login_button.click()

    with allure.step("Check that 'Nice to meet you!' message is displayed"):
        assert login_dialog.nice_to_message.is_displayed(), "'Nice to meet you!' message is not displayed"
