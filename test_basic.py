import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Don't forget to start the server first


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

    # Edith notices the page header mentions to-do lists
    header_text = browser.find_element_by_tag_name('h1').text
    assert 'To-Do' in header_text

    # She is invited to enter a to-do item straight away
    inputbox = browser.find_element_by_id('id_new_item')
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

    # She types "Buy peacock feathers" into a text box
    inputbox.send_keys('Buy peacock feathers')

    # When she hits Enter, the page updates and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)

    table = browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    assert any(row.text == '1: Buy peacock feathers' for row in rows)

    assert "You're done" == "Finish the test!!"
