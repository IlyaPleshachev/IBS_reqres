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

    def get_request_payload(self):
        # header_text и payload_text - мы отправляем
        header_text = self.browser.find_element(*BasePageLocators.REQUEST_HEADER).text
        payload_text = self.browser.find_element(*BasePageLocators.REQUEST_PAYLOAD).text.replace('\n', '').replace(' ', '')
        # response_code и response_content - мы получаем
        response_code = self.browser.find_element(*BasePageLocators.RESPONSE_CODE).text
        response_content = self.browser.find_element(*BasePageLocators.RESPONSE_CONTENT).text.replace('\n', '').replace(' ', '')
        return header_text, payload_text, response_code, response_content

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

    # Api functions
    def get_list_users(self):
        URL = 'https://reqres.in/api/users?page=2'
        api_response = requests.get(URL)
        data = {"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
        print(data)
        print('-----------')
        print(api_response.status_code)
        print(api_response.json())

        assert api_response.status_code == 200, 'Status code is not 200'
        assert api_response.json() == data, 'Response json is not equal example'

    # Запрос отправляет только header
    def send_request_header_only(self):
        pass
    # Запрос отправляет header и payload
    def send_request_header_and_payload(self):
        pass

