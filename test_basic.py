import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')
    browser.implicitly_wait(2)

    yield browser

    browser.close()


def test_title(browser):
    assert 'To-Do' in browser.title


def test_edith_story(browser):
    pass
