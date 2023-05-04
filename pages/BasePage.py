import time
from pages.locators import BasePageLocators
import requests

class BasePage():
    # Web functions
    def __init__(self, browser, url, timeout = 4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    def go_to_list_users(self):
        link = self.browser.find_element(*BasePageLocators.LINK_GET_LIST_USERS)
        link.click()

    def go_to_create_new_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_CREATE_NEW_USER)
        link.click()

    def go_to_update_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_UPDATE_USER)
        link.click()

    def go_to_delete_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_DELETE_USER)
        link.click()



