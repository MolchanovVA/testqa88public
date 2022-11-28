from pages.auth_page import AuthPage
import time

def test_auth_page(selenium):
    page = AuthPage
    page.enter_email("email@gmail.com")
    page.enter_pass("pass")
    page.btn_click()

    assert page.get_relative_link() != '/all_pets', "login error"

    time.sleep(5)