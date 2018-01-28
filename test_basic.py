import pytest
from selenium import webdriver
import subprocess as sp


# Start server
sp.Popen(['python', 'manage.py', 'runserver'])


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000')

    yield browser

    browser.close()


def test_title(browser):
    assert 'Django' in browser.title
