from pages.BasePage import BasePage
import pytest

link = 'https://reqres.in/'

class Test_with_webdriver():

    def test_get_list_users(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_list_users()
        print(page.get_request_payload())


    @pytest.mark.skip
    def test_create_new_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_create_new_user()
        print(page.get_request_payload())

    @pytest.mark.skip
    def test_update_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_update_user()
        print(page.get_request_payload())

    @pytest.mark.skip
    def test_delete_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_delete_user()
        print(page.get_request_payload())