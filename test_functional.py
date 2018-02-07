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


def enter_new_item(browser, item_text):
    inputbox = browser.find_element_by_id('id_new_item')
    inputbox.send_keys(item_text)
    inputbox.send_keys(Keys.ENTER)


def check_for_row_in_list_table(browser, search_text):
    table = browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    return any(row.text == search_text for row in rows)


def test_edith_story(browser):

    # Edith notices the page header mentions to-do lists.
    header_text = browser.find_element_by_tag_name('h1').text
    assert 'To-Do' in header_text

    # She is invited to enter a to-do item straight away.
    inputbox = browser.find_element_by_id('id_new_item')
    assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

    # She enters an item. The page updates and the item appears in a table.
    first_item = 'Buy peacock feathers'
    enter_new_item(browser, first_item)
    assert check_for_row_in_list_table(browser, '1: {}'.format(first_item))

    # There is still a text box inviting her to add another item.
    # She enters another item.
    second_item = 'Use peacock feathers to make a fly'
    enter_new_item(browser, second_item)

    # The page updates again, and now shows both items on her list.
    assert check_for_row_in_list_table(browser, '1: {}'.format(first_item))
    assert check_for_row_in_list_table(browser, '2: {}'.format(second_item))

    assert "You're done" == "Finish the test!!"
