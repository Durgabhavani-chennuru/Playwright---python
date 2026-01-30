'''must start with test
# playwright is an  global fixture
from pytest_playwright.pytest_playwright import browser'''

import pytest_playwright
from playwright.sync_api import Page

import time

from pytest_playwright.pytest_playwright import browser


# amazon login page
def test_coreLocators(page:Page):
    page.goto("https://www.amazon.in/")
    page.get_by_role("link",name= "Account & Lists").click()
    page.get_by_label("Enter mobile number or email").type("durgabhavanichennuru3@gmail.com") # input type
    page.click("#continue")  #continue is id so we need to start with #
    page.get_by_label("Password").type("Chennuru@123")
    page.click("#signInSubmit")







































