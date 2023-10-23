import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_desktop():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture(scope="function")
def browser_mobile():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 320
    browser.config.window_height = 593

    yield

    browser.quit()
