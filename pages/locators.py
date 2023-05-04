from selenium.webdriver.common.by import By

class BasePageLocators():
    # Локаторы кнопок запросов
    LINK_GET_LIST_USERS = (By.CSS_SELECTOR, '[data-id="users"]')
    LINK_CREATE_NEW_USER = (By.CSS_SELECTOR, '[data-id="post"]')
    LINK_UPDATE_USER = (By.CSS_SELECTOR, '[data-id="put"]')
    LINK_DELETE_USER = (By.CSS_SELECTOR, '[data-id="delete"]')

    # Запрос и полезная нагрузка
    REQUEST_HEADER = (By.CSS_SELECTOR, '[data-key="url"]')
    REQUEST_PAYLOAD = (By.CSS_SELECTOR, '[data-key="output-request"]')

    # Код ответа и тело ответа
    RESPONSE_CODE = (By.CSS_SELECTOR, '[data-key="response-code"]')
    RESPONSE_CONTENT = (By.CSS_SELECTOR, '[data-key="output-response"]')

