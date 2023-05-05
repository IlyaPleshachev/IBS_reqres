import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    """-Setup & -Teardown fixture func"""
    print('\nStarting browser before test')
    browser = webdriver.Chrome()
    yield browser
    print('\nClosing browser after test')
    browser.quit()
