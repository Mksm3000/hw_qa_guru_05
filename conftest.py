import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com/"
    browser.config.window_width = 1600
    browser.config.window_height = 900

    yield
    browser.quit()
