from pages.BasePage import BasePage
import pytest



link = 'https://reqres.in/'

class Test_with_webdriver():

    def test_get_list_users(self, browser):
        pass

    @pytest.mark.skip
    def test_create_new_user(self, browser):
        pass

    @pytest.mark.skip
    def test_update_user(self, browser):
        pass

    @pytest.mark.skip
    def test_delete_user(self, browser):
        pass