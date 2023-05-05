from pages.BasePage import BasePage
from pages.Api_BasePage import Api_BasePage
import pytest

link = 'https://reqres.in/'
@pytest.mark.api
class Test_with_API():
    @pytest.mark.get_list
    def test_api_get_list_users(self):
        Api_BasePage.get_list_users(self)

    @pytest.mark.create
    def test_api_create_new_user(self):
        Api_BasePage.create_new_user(self)

    @pytest.mark.update
    def test_update_user(self):
        Api_BasePage.update_user(self)

    @pytest.mark.delete
    def test_delete_users(self):
        Api_BasePage.delete_user(self)
    @pytest.mark.xfail
    def test_unhappy_register(self):
        Api_BasePage.unhappy_register(self)

@pytest.mark.web
class Test_with_webdriver():
    """Several tests with webdriver
    - Get list users
    - Create user
    - Update user
    - Delete user
    """
    @pytest.mark.get_list
    def test_get_list_users(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_list_users()
        web_answer = page.get_request_payload()
        api_answer = Api_BasePage.get_list_users(self)
        assert int(web_answer[2]) == api_answer[0], 'Web and api requests arent equal'

    @pytest.mark.create
    def test_create_new_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_create_new_user()
        web_answer = page.get_request_payload()
        api_answer = Api_BasePage.create_new_user(self)
        assert int(web_answer[2]) == api_answer[0], 'Web and api requests arent equal'

    @pytest.mark.update
    def test_update_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_update_user()
        web_answer = page.get_request_payload()
        api_answer = Api_BasePage.update_user(self)
        assert int(web_answer[2]) == api_answer[0], 'Web and api requests arent equal'

    @pytest.mark.delete
    def test_delete_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_delete_user()
        web_answer = page.get_request_payload()
        api_answer = Api_BasePage.delete_user(self)
        assert int(web_answer[2]) == api_answer, 'Web and api requests arent equal'


