import pytest

def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element_by_class_name('btn-add-to-basket')