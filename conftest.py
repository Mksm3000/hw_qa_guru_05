import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"

    # we want to type text via JavaScript to speed up tests a bit
    browser.config.type_by_js = True

    browser.config.window_width = 1600
    browser.config.window_height = 900
    # browser.config.timeout = 7

    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument("--headless=new")

    browser.config.driver_options = driver_options

    yield

    browser.quit()
