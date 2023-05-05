import time
from pages.locators import BasePageLocators

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
        time.sleep(1)
    def go_to_create_new_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_CREATE_NEW_USER)
        link.click()
        time.sleep(1)
    def go_to_update_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_UPDATE_USER)
        link.click()
        time.sleep(1)
    def go_to_delete_user(self):
        link = self.browser.find_element(*BasePageLocators.LINK_DELETE_USER)
        link.click()
        time.sleep(1)

    def get_request_payload(self):
        # header_text и payload_text - мы отправляем
        header_text = self.browser.find_element(*BasePageLocators.REQUEST_HEADER).text
        payload_text = self.browser.find_element(*BasePageLocators.REQUEST_PAYLOAD).text.replace('\n', '')
        # response_code и response_content - мы получаем
        response_code = self.browser.find_element(*BasePageLocators.RESPONSE_CODE).text
        response_content = self.browser.find_element(*BasePageLocators.RESPONSE_CONTENT).text.replace('\n', '')
        return (header_text, payload_text, response_code, response_content)
