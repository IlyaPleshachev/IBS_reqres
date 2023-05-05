from pages.BasePage import BasePage
from pages.Api_BasePage import Api_BasePage
import pytest

link = 'https://reqres.in/'

class Test_with_webdriver():
    """Several tests with webdriver
    - Get list users
    - Create user
    - Update user
    - Delete user
    """
    #@pytest.mark.skip
    def test_get_list_users(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_list_users()
        print(page.get_request_payload())

    #@pytest.mark.skip
    def test_create_new_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_create_new_user()
        web_answer = page.get_request_payload()
        api_answer = Api_BasePage.create_new_user(self)
        print('\nPrintin web answer', web_answer)
        print('\nPrintin api answer', api_answer)
        assert int(web_answer[2]) == api_answer[0], 'Not equal'

    #@pytest.mark.skip
    def test_update_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_update_user()
        print(page.get_request_payload())

    #@pytest.mark.skip
    def test_delete_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_delete_user()
        print(page.get_request_payload())

class Test_with_API():
     def test_api_get_list_users(self):
        api_answer = Api_BasePage.get_list_users(self)
     def test_api_create_new_user(self):
        api_answer = Api_BasePage.create_new_user(self)
     def test_update_user(self):
        api_answer = Api_BasePage.update_user(self)
     def test_delete_users(self):
        api_answer = Api_BasePage.delete_user(self)
