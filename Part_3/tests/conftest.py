from selene import browser
import pytest


@pytest.fixture(scope='function')
def windows_size():
    browser.config.window_height = 1200
    browser.config.window_width = 800
    yield
    browser.quit()
