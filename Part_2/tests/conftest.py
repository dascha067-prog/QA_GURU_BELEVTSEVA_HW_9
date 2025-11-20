import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1200
    browser.config.window_height = 800
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6

    yield

    browser.quit()
