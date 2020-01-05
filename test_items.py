from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_found_add_item_button(browser):
    LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(LINK)

    add_button = (By.CSS_SELECTOR, "form[id='add_to_basket_form'] button[type='submit']")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located(add_button))

    assert len(browser.find_elements_by_css_selector(
        "form[id='add_to_basket_form'] button[type='submit']")) == 1, 'added button should be only one'
